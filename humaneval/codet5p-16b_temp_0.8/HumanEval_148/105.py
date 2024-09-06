
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

    orbit = {
        "Mercury": 0.387,
        "Venus": 0.723,
        "Earth": 1,
        "Mars": 1.523,
        "Jupiter": 11.86,
        "Saturn": 29.447,
        "Uranus": 84.0168,
        "Neptune": 164.79132
    }
    planet_orbit = orbit.get(planet1, None)
    planet_orbit2 = orbit.get(planet2, None)
    if planet_orbit is None or planet_orbit2 is None:
        return tuple()
    all_planets = orbit.keys()
    all_planets = sorted(all_planets, key=lambda x: abs(orbit[x]-planet_orbit2))
    all_planets = sorted(all_planets, key=lambda x: abs(orbit[x]-planet_orbit))
    return tuple(all_planets)

