from levenshtein import levenshtein

with open("british-english.txt") as fh:
    words = [line.strip() for line in fh]


def get_neighbors(data, check, k, distance):
    return sorted([(w, distance(check, w)) for w in data], key=lambda x: x[1])[:k]


test_list = ['holp']
for test in test_list:
    result = get_neighbors(data=words, check=test, k=3, distance=levenshtein)
    print(test, result)
