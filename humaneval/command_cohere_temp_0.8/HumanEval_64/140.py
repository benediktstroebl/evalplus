```python
 FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    count = 0
    for char in s:
        if char in 'aieou':
            count += 1
        elif char == 'y' and s.endswith(char):
            count += 1
    return count

# MAIN ARISING TEST CASES

def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("Hello") == 3
    assert vowels_count("World") == 1
    assert vowels_count("NY") == 1
    assert vowels_count("ayu") == 3
    assert vowels_count("ky") == 1
    assert vowels_count("sky") == 2
    assert vowels_count("py") == 1
    assert vowels_count("spy") == 2
    assert vowels_count("friday") == 3
    assert vowels_count("data") == 3
    assert vowels_count("science") == 4
    assert vowels_count("unit") == 2
    assert vowels_count("unity") == 3
    assert vowels_count("toxic") == 3
    assert vowels_count("radar") == 3
    assert vowels_count("colony") == 3
    assert vowels_count("vega") == 2
    assert vowels_count("nova") == 2
    assert vowels_count("quotient") == 4
    assert vowels_count("entropy") == 4
    assert vowels_count("isotope") == 4
    assert vowels_count("hierarchy") == 5
    assert vowels_count("idiosyncrasy") == 6
    assert vowels_count("hyperbolism") == 6
    assert vowels_count("pythagoreanism") == 7
    assert vowels_count("paradigm") == 4
    assert vowels_count("lexicon") == 4
    assert vowels_count(" academy") == 4
    assert vowels_count("concord") == 3
    assert vowels_count(" symphony") == 4
    assert vowels_count("monopoly") == 4
    assert vowels_count("oly") == 3
    assert vowels_count("dry") == 1
    assert vowels_count("dye") == 2
    assert vowels_count("eye") == 2
    assert vowels_count("barracuda") == 4
    assert vowels_count("nightmare") == 4
    assert vowels_count("espresso") == 4
    assert vowels_count("alfalfa") == 3
    assert vowels_count("chiliblain") == 4
    assert vowels_count("leucorrhoea") == 5
    assert vowels_count("omnipotent") == 5
    assert vowels_count(" empathize") == 5
    assert vowels_count("library") == 4
    assert vowels_count("vocabulary") == 5
    assert vowels_count("laboratory") == 5
    assert vowels_count("concatenate") == 5
    assert vowels_count("acceleration") == 5
    assert vowels_count("favourite") == 4
    assert vowels_count("GRAVE") == 3
    assert vowels_count("lobotomy") == 3
    assert vowels_count("skeleton") == 3
    assert vowels_count("ostracod") == 3
    assert