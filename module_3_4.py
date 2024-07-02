# Произвольное число параметров

def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        for j in range(len(i) - len(root_word)):
            if i[j:len(root_word) + j].upper() == root_word.upper():
                same_words.append(i)
                break
        for j in range(len(root_word) - len(i)):
            if root_word[j:len(i) + j].upper() == i.upper():
                same_words.append(i)
                break
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
