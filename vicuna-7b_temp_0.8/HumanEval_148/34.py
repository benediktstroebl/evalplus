
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
    # Check if planet1 and planet2 are valid planet names
    if not (planet1 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]):
        return []
    if not (planet2 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]):
        return []
    # Check if the orbit of planet1 is closer to the sun
    if (planet1 < planet2) or (planet1 == planet2):
        planets = [planet1]
    else:
        planets = [planet2]
    # Check if the orbit of planet2 is closer to the sun
    if (planet2 < planet1) or (planet2 == planet1):
        planets.append(planet1)
    else:
        planets.append(planet2)
    planets.sort(key=lambda planet: (planet.get_distance_to_sun(),))
    return tuple(planets)
