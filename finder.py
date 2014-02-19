import random, string
words = []
count = 0
f = open('/usr/share/dict/words')
for itm in f.readlines():
    words.append(itm.strip().lower())
word = raw_input("What word do you want found?").lower()
if word in words:
    random_word = random.choice(words)
    while word != random_word:
        random_word = random.choice(words)
        count +=1
        print "Count: %d | Word: %s" % (count, random_word)
    else:
        print "It took " + str(count) + " tries to find the word: " + str(word) + "."
else:
    print "Please clarify your input."