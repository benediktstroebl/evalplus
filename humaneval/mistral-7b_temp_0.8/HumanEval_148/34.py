
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
    planets = {
        "Mercury": "planet 1",
        "Venus": "planet 2",
        "Earth": "planet 3",
        "Mars": "planet 4",
        "Jupiter": "planet 5",
        "Saturn": "planet 6",
        "Uranus": "planet 7",
        "Neptune": "planet 8"
    }
    planet1 = planets[planet1]
    planet2 = planets[planet2]
    return tuple(planets.keys())[planets[planet1] : planets[planet2]]

