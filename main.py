
dict_L33t = {
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

def eng_L33t(string:str):
    ans = string
    for ch in string:
        ans = ans.replace(ch, dict_L33t[ch])
    print ('Translated phrase:')
    print (ans)

def L33t_eng(string:str):
    ans = string
    for el in dict_L33t.values():
        ans = ans.replace(el, list(dict_L33t.keys())[list(dict_L33t.values()).index(el)])
    print ('Translated phrase:')
    print (ans)


def english_to_L33t(string:str):
    ans = []
    for ch in string:
        if ch in dict_L33t.keys():
            ans.append(dict_L33t[ch])
        else:
            print('Unknown character: ', ch)
    print ('Translated phrase:')
    print (''.join(ans))

def L33t_to_english(string:str):
    ans = []
    revdict = {v: k for k, v in dict_L33t.items()}
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
    print ('Translated phrase:')
    print (''.join(ans))

def translating():
    phrase = str(input('Enter phrase: ')).lower()

    diff = ['1','3','4','5','6','7','/','(',')','`']

    leet = None

    if phrase:
        for ch in phrase:
            if ch in diff:
                leet = True
                break

        if leet:
            L33t_eng(phrase)
        else:
            eng = input('Is the phrase in english? (y/n): ')
            if eng == 'n':
                L33t_eng(phrase)
            elif eng == 'y':
                eng_L33t(phrase)


translating()
