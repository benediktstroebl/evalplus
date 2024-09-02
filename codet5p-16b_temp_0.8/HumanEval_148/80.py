
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

    planets = {"Mercury": 3.303e+23, "Venus": 6.051e+24, "Earth": 6.371e+24,
    "Mars": 3.389e+23, "Jupiter": 1.899e+27, "Saturn": 5.688e+26,
    "Uranus": 8.681e+25, "Neptune": 1.024e+26}
    result = ()
    for planet in planets.keys():
        if planet == planet1 or planet == planet2:
            continue
        if planets[planet1] < planets[planet] < planets[planet2]:
            result += (planet,)
    return result

