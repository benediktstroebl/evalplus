
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

    import math
    planets = {
        "Mercury": [0, 4879],
        "Venus": [0, 10821],
        "Earth": [0, 1495987870],
        "Mars": [1.5e9, 679.9e6],
        "Jupiter": [4.5e9, 43444.8],
        "Saturn": [9.4e9, 93326.4],
        "Uranus": [5.6e9, 82164.8],
        "Neptune": [1.7e9, 51118.1]
    }

    for i in planets:
        if planet1 == i:
            p1 = planets[i]

    for j in planets:
        if planet2 == j:
            p2 = planets[j]

    dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    result = []
    if dist == 0:
        return tuple(sorted(planets.keys()))
