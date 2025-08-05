import argparse
import csv
import urllib.request
import os

parser = argparse.ArgumentParser()
parser.add_argument('name', type=str)
parser.add_argument('-d', action='store_true')


def load():
    with open('emoji-urls.csv', mode='r') as infile:
        reader = csv.reader(infile)
        return dict((rows[0], rows[1]) for rows in reader)


def download(name, url):
    ext = url.rsplit(".", 1)[1]
    dest_file = "results/" + name + "." + ext
    if os.path.isfile(dest_file):
        return
    print ('downloading...\t' + dest_file)
    urllib.request.urlretrieve(url, "results/" + name + "." + ext)


def ensure_results_dir():
    if not os.path.exists("results"):
        os.makedirs("results")

def main():

    args = parser.parse_args()
    print(args.d)
    print("looking for: [" + args.name + "]")
    idx = 0
    emojis = load()
    keys = emojis.keys()
    if args.d:
        ensure_results_dir()
    for key in keys:
        if args.name in key:
            print(key + "\n-------------\n" + emojis[key]+'\n')
            if args.d:
                download(key, emojis[key])


if __name__=="__main__":
    main()