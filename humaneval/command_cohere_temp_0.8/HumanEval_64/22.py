```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Returns the number of vowels in a string s,
    including special case for 'y' as a vowel at the end of the word."""
    vowels = 'aeiouy'
    return sum(1 for char in s if char in vowels)

def test_vowels_count():
    assert vowels_count("acedy") == 3
    assert vowels_count("fried") == 1
    assert vowels_count("joy") == 2
    assert vowels_count("caesar") == 3
    assert vowels_count("braid") == 2
    assert vowels_count("abstract") == 3
    assert vowels_count("roast") == 1
    assert vowels_count("century") == 3
    assert vowels_count("fittingly") == 3
    assert vowels_count("melon") == 1
    assert vowels_count("gulch") == 1
    assert vowels_count("closer") == 2
    assert vowels_count("bridge") == 3
    assert vowels_count("trust") == 1
    assert vowels_count("pretend") == 3
    assert vowels_count("vest") == 1
    assert vowels_count("skiing") == 3
    assert vowels_count("zoo") == 3
    assert vowels_count("cars") == 2
    assert vowels_count("harass") == 3
    assert vowels_count("cohere") == 3
    assert vowels_count("no") == 1
    assert vowels_count("terrible") == 3
    assert vowels_count("ruby") == 2
    assert vowels_count("ply") == 1
    assert vowels_count("league") == 3
    assert vowels_count("me") == 2
    assert vowels_count("barren") == 3
    assert vowels_count("wagon") == 2
    assert vowels_count("green") == 3
    assert vowels_count("bluff") == 2
    assert vowels_count("sulfur") == 3
    assert vowels_count("gravity") == 3
    assert vowels_count("pilot") == 3
    assert vowels_count("pirate") == 3
    assert vowels_count("rogue") == 3
    assert vowels_count("gladiator") == 4
    assert vowels_count("sublime") == 4
    assert vowels_count("test") == 1
    assert vowels_count("case") == 2
    assert vowels_count("reflex") == 3
    assert vowels_count("statue") == 3
    assert vowels_count("stench") == 3
    assert vowels_count("fatal") == 3
    assert vowels_count("grace") == 3
    assert vowels_count("treasure") == 4
    assert vowels_count("sanctuary") == 4
    assert vowels_count("oval") == 2
    assert vowels_count("park") == 2
    assert vowels_count("twenty") == 3
    assert vowels_count("awful") == 3
    assert vowels_count("bliss") == 3
    assert vowels_count("gusto") == 3
    assert vowels_count("regal") == 3
    assert vowels_count("saunter") == 4
    assert vowels_count("generative") == 4
    assert vowels_count("miracle") == 4
    assert vowels_count("pinot") == 3
    assert vowels_count("glamor") == 3
    assert vowels_count("burden") == 3
    assert vowels_count("moniker") == 3
    assert vowels_count("rover") == 2
    assert vowels_count("sentry") == 3
    assert vowels_count("vigil") == 3