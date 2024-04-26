import re

def ex():
    text = 'push code everyday!'
    pattern = r'\b(c*.)\b'

    # regex search: use pattern to find matches in text

    # compile pattern in to regex object reObj
    reObj = re.compile(pattern)

    # print results of search
    print(reObj.search(text))

if __name__ == "__main__":
    ex()