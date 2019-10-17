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
    owner='pdswift'
    repo="CI-CD-Flaskr-Pipeline"
    github_endpoint = "https://api.github.com/repos/%s/%s/commits" % (owner, repo)
    previous_time="1999-12-31T23:59:59Z"
    with open('./config','r') as f:
        buffer=f.read()
        if buffer:
            previous_time=f.read()

    args = {'since':previous_time}

    response = requests.get(github_endpoint, params=args)
    for item in response.json():
        if previous_time<item['commit']['author']['date']:
            print('new commit found!')
            previous_time=item['commit']['author']['date']
            with open('./config', 'w') as f:
                f.write(previous_time)
            download_repo()


if __name__ == '__main__':
    main()
