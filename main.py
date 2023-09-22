import time

import vk_api
from time import sleep


vk_session = vk_api.VkApi(
    token="vk1.a.c--hKQcemvT8EQpH5yKfObEHKVUvS69r0piv_DRRFP4MuT-lJ50zxi7JO5agd5k2v4yJbE2l6CHvgxW18jvMEul64BljY6oLQaPI7kq9eeqRA_Sv3JbpTSWh2md7bxzj0nArRHzs48vUVdA9ael1f8geYBMLjHWybBluG6yq_f-Ma-fu3n4MjqLoKv29EkIfux9TLpVDjU_ifT_rAwGz5Q"
)
api = vk_session.get_api()
message = open("text.txt").readlines()


def post_all():
    with open("groups.txt") as groups:
        with open("text.txt") as text:
            for group in groups.readlines():
                try:
                    api.wall.post(
                        owner_id=-int(group.strip()),
                        message=message,
                        attachments="photo621644670_457250961",
                    )
                    links = api.groups.getById(
                        group_id=-int(group.strip()), fields="links"
                    )
                    print(f"Posted in: {links[0]['name']} ({links[0]['url']})")
                    sleep(1)
                except Exception as e:
                    print(str(e))


def get_last_sent():
    try:
        with open("last_sent.txt", "r") as f:
            return int(f.read().strip())
    except Exception:
        save_last_sent(0)
        return get_last_sent()


def save_last_sent(time: int):
    with open("last_sent.txt", "w") as f:
        f.write(str(time))


def main():
    last_sent = get_last_sent()
    while True:
        if round(time.time()) - last_sent >= 86400:
            print("Starting posting!")
            post_all()
            last_sent = time.time()
            save_last_sent(round(last_sent))
            print(f"Last posted timestamp: {last_sent}")
        else:
            print("Sleeping for 60s...")
            sleep(60)


def test_post():
    api.wall.post(
        owner_id=-218040116, message="test", attachments="photo621644670_457250961"
    )


if __name__ == "__main__":
    main()
