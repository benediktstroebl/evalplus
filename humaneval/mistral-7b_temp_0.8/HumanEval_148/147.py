
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

    def is_planet(planet):
        return planet == "Mercury" or planet == "Venus" or planet == "Earth" or planet == "Mars" or planet == "Jupiter" or planet == "Saturn" or planet == "Uranus" or planet == "Neptune"

    if not is_planet(planet1) or not is_planet(planet2):
        return ()
    else:
        planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        planet_index = planets.index(planet1)
        return tuple(planets[planet_index:planets.index(planet2) + 1])





































































