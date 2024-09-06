
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
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return tuple()
    if planet1 == "Jupiter" or planet2 == "Jupiter":
        return tuple()
    if not any(planet1.lower() in name.lower() for name in ["jupiter", "saturn", "uranus", "neptune"]) and not any(planet2.lower() in name.lower() for name in ["jupiter", "saturn", "uranus", "neptune"]):
        return tuple()
    if not any(planet1.lower() in name.lower() for name in ["venus", "earth", "mars", "mercury"]):
        return tuple()
    if not any(planet2.lower() in name.lower() for name in ["mercury", "earth", "mars", "venus"]):
        return tuple()
    orbit_data = [(planet, distance(planet1, planet)) for planet in planet1.lower().split() + planet2.lower().split()]
    orbit_data.sort(key=lambda x: distance(x[0], planet1))
    orbit_data = orbit_data[:-2] + orbit_data[-2:]
    orbit_data.sort(key=lambda x: distance(planet1, x[0]))
    orbit_data = orbit_data[1:]
    return tuple(orbit_data)