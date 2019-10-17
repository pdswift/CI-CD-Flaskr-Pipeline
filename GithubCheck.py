# Checks Github for Updates
import requests


def download_repo():
    repo_endpoint = 'https://api.github.com/repos/%s/%s/%s/' % ("billerhard","CI-CD-Flaskr-Pipeline", 'zipball')
    args={}
    response = requests.get(repo_endpoint,params=args)
    with open('./repo.zip', "wb") as f:
        f.write(response.content)


def main():
    # do stuff
    github_endpoint = "https://api.github.com/repos/%s/%s/commits" % ("billerhard", "CI-CD-Flaskr-Pipeline")
    previous_time="2019-10-17T01:01:01Z"
    args = {'since':previous_time}

    response = requests.get(github_endpoint, params=args)
    for item in response.json():
        if previous_time<item['commit']['author']['date']:
            print('new commit found!')
            previous_time=item['commit']['author']['date']
            download_repo()


if __name__ == '__main__':
    main()
