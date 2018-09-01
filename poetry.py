import random

nouns = ['fossil', 'horse', 'aardvardk', 'judge', 'chef', 'mango', 'extrovert',
        'gorilla']

verbs = ['kicks', 'jingles', ' bounces', 'slurps', 'meows', 'explodes', 'curdles']

adjectives = ['furry', 'balding', 'incredulous', 'fragrant', 'exuberant', 'glistening']

prepositions = ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like',
                'over', 'within']

adverbs = ['curiously', 'extravagantly', 'tantalizingly', 'furiously', 'sensuously']


def make_poem(nouns, verbs, adjectives, prepositions, adverbs):
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    noun3 = random.choice(nouns)
    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    adj3 = random.choice(adjectives)
    verb1 = random.choice(verbs)
    verb2 = random.choice(verbs)
    verb3 = random.choice(verbs)
    prep1 = random.choice(prepositions)
    prep2 = random.choice(prepositions)
    adv1 = random.choice(adverbs)

    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't' 'v', 'w', 'x', 'y', 'z']
    a_an = ''

    if adj1[0].lower() in consonants:
        a_an = 'A'
    else:
        a_an = 'An'

    if adj3[0] in consonants:
        a_an2 = 'a'
    else:
        a_an2 = 'an'

    return(f"""
    {a_an} {adj1} {noun1}

    {a_an} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
    {adv1}, the {noun1} {verb2}
    the {noun2} {verb3} {prep2} {a_an2} {adj3} {noun3}
    """)

my_output = open("poetry.txt", "w")

for i in range(1, 6):  
    poem = make_poem(nouns, verbs,adjectives, prepositions, adverbs)
    my_output.writelines(poem)

my_output.close()

with open("poetry.txt", "r") as an_input, open("poetryCopy.txt", "w") as an_output:
    for line in an_input.readlines():
        an_output.write(line)
    