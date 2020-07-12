def find_anagrams(word, candidates):
    word = word.casefold()

    return [c for c in candidates
            if sorted(c.casefold()) == sorted(word)
            and c.casefold() != word]
