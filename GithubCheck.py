# Checks Github for Updates
import requests


def main():
    # do stuff
    master="957acb944661f8ba6b462381fc719a79b1a6fd3d"
    github_endpoint = "https://api.github.com/repos/%s/%s/commits" % ("billerhard", "CI-CD-Flaskr-Pipeline")
    previous_time="2019-10-17T01:01:01Z"
    args = {'sha':master, 'since':previous_time}

    response = requests.get(github_endpoint, params=args)
    print(response)
    print(response.json())


if __name__ == '__main__':
    main()
