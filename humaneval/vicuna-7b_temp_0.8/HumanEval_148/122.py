
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
    def __check_planets(planet):
        if not isinstance(planet, str):
            return None
        elif planet == "Mercury" or planet == "Venus" or \
             planet == "Earth" or planet == "Mars" or planet == "Jupiter" or \
             planet == "Saturn" or planet == "Uranus" or planet == "Neptune":
            return planet
        else:
            return None

    def __sort_planets(planets):
        if len(planets) > 1:
            return sorted(planets, key=lambda planet: 
                         abs(planet.distance(planet1)) - abs(planet.distance(planet2)))
        else:
            return planets

    def __is_correct_planet(planet):
        return planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", 
                         "Uranus", "Neptune"]

    planet1 = __check_planets(planet1)
    planet2 = __check_planets(planet2)

    if not planet1 or not planet2:
        return ()

    planets = __sort_planets([__is_correct_planet(planet), __is_correct_planet(planet2)])

    return planets
