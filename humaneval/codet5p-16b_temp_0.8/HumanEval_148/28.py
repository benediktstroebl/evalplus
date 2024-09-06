
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''

    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    assert planet1 in planets, "No planet with name {}".format(planet1)
    assert planet2 in planets, "No planet with name {}".format(planet2)
    if planet1 == planet2:
        return ()
    if planet1 == "Mercury":
        result = []
        for i in range(8):
            if planets[i]!= planet1 and planets[i]!= planet2:
                result.append(planets[i])
        return (result[0], result[-1])
    if planet1 == "Venus":
        result = []
        for i in range(7):
            if planets[i]!= planet1 and planets[i]!= planet2:
                result.append(planets[i])
        return (result[0], result[-1])
    if planet1 == "Earth":
        result = []
        for i in range(6):
            if planets[i]!= planet1
