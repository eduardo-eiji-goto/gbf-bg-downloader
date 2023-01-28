#!/usr/bin/python3

import requests


def downloadPicture(url: str):
    with open(url.split('/')[-1], 'wb') as handle:
        response = requests.get(url)

        if response.ok:
            handle.write(response.content)
        else:
            raise Exception('Image not found!')
        handle.close()


def main():

    c = 1

    while True:
        try:
            downloadPicture(
                'https://prd-game-a-granbluefantasy.akamaized.net/assets/img/sp/top/bg/bg_' +
                str(c) + '.jpg'
            )
            c += 1
        except:
            break


if __name__ == '__main__':
    main()
