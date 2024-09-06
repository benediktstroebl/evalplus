
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
    if not planet1.lower() == "mercury" and not planet2.lower() == "jupiter":
        return []
    
    elif not (planet1.lower() in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"] or 
               planet2.lower() in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]):
        return []
    
    orbit_planets = []
    for planet in [planet1, planet2]:
        if planet in ["earth", "mars", "jupiter", "saturn", "uranus", "neptune"]:
            orbit_planets.append(planet)
        elif planet not in ["mercury", "venus"]:
            orbit_planets.append(planet)
    return orbit_planets
