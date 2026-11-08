def countwords(extract : str) -> int:
    wlist = extract.split()
    return len(wlist)

def convtodict (extract : str) -> dict[str, int]:
    worddict = {}
    extract = extract.lower()
    for char in extract:
        if char in worddict:
            worddict[char] += 1
        else:
            worddict[char] = 1

    return worddict

def sort_on (wordtuple : tuple[str, int]) -> int:
    return wordtuple[1]

def chars_dict_to_sorted_list (worddict : dict[str, int]) -> list[tuple[str,int]]:
    newlist = []
    for entry in worddict:
        newlist.append((entry,worddict[entry]))

    return (sorted(newlist, key=sort_on, reverse = True))
