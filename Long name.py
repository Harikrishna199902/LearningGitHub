 


def LongNameAndLen(word):
    string = ''
    for item in word:
        if len(item)>len(string):
            string = item

    return string, len(string)
n = ['Harikrishna','tejajuvvala']
print(LongNameAndLen(n))

