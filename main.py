# pylint: disable=W1401, C0114, C0116

dict_l33t = {
    'a': '4',
    'b': '6',
    'c': 'c',
    'd': 'd',
    'e': '3',
    'f': 'f',
    'g': 'g',
    'h': 'h',
    'i': '1',
    'j': 'j',
    'k': 'k',
    'l': '|',
    'm': '(v)',
    'n': '(\)',
    'o': '0',
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': '5',
    't': '7',
    'u': 'u',
    'v': '\/',
    'w': '`//',
    'x': 'x',
    'y': 'y',
    'z': 'z',
    ' ': ' '
}


# new methods

def eng_l33t(string: str):
    ans = string
    for char in string:
        ans = ans.replace(char, dict_l33t[char])
    print('Translated phrase:')
    print(ans)


def l33t_eng(string: str):
    revdict = {v: k for k, v in dict_l33t.items()}
    for elem in revdict:
        string = string.replace(elem, revdict[elem])
    print('Translated phrase:')
    print(string)


# old methods

def english_to_l33t(string: str):
    ans = []
    for char in string:
        if char in dict_l33t:
            ans.append(dict_l33t[char])
        else:
            print('Unknown character: ', char)
    print('Translated phrase:')
    print(''.join(ans))


def l33t_to_english(string: str):
    ans = []
    revdict = {v: k for k, v in dict_l33t.items()}
    i = 0
    while i < len(string):
        if string[i] in revdict.keys():
            ans.append(revdict[string[i]])
            i += 1
        elif string[i:i+2] in revdict.keys():
            ans.append(revdict[string[i:i+2]])
            i += 2
        elif string[i:i+3] in revdict.keys():
            ans.append(revdict[string[i:i+3]])
            i += 3
        else:
            print('Unknown character')
            i += 1
    print('Translated phrase:')
    print(''.join(ans))


def translating():
    phrase = str(input('Enter phrase: ')).lower()

    diff = ['1', '3', '4', '5', '6', '7', '/', '(', ')', '`']

    leet = None

    if phrase:
        for char in phrase:
            if char in diff:
                leet = True
                break

        if leet:
            l33t_eng(phrase)
        else:
            eng = input('Is the phrase in english? (y/n): ')
            if eng == 'n':
                l33t_eng(phrase)
            elif eng == 'y':
                eng_l33t(phrase)


translating()
