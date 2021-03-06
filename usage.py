from pybo import *


###########################################
tok = BoTokenizer('POS')  # instanciated
tok.tok.trie.rebuild_trie()

input_str = ' ཤི་བཀྲ་ཤིས་  tr བདེ་་ལེ གས། བཀྲ་ཤིས་བདེ་ལེགས་ཀཀ'
tokens = tok.tokenize(input_str)
###########################################


### Extract token-string / POS pairs ########

tagged = ['"{}"/{}'.format(w.content, w.pos) for w in tokens]
print(', '.join(tagged))
# " ཤི་"/VERB, "བཀྲ་ཤིས་  "/NOUN, "tr"/non-bo, " བདེ་་ལེ གས"/NOUN, "།"/punct,
# " བཀྲ་ཤིས་"/NOUN, "བདེ་ལེགས་"/NOUN, "ཀཀ"/non-word


### Extract the cleaned version of the tokens

cleaned = [w.cleaned_content for w in tokens if w.cleaned_content]
print(' '.join(cleaned))
# ཤི་ བཀྲ་ཤིས་ བདེ་ལེགས་ བཀྲ་ཤིས་ བདེ་ལེགས་ ཀཀ་


### The fields found in each token ###########

print(tokens[0])
# content: " ཤི་"
# char types: |space|cons|vow|tsek|
# type: syl
# start in input: 0
# length: 4
# syl chars in content(ཤི): [[1, 2]]
# tag: VERBᛃᛃᛃ
# POS: VERB
