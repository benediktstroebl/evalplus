
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
    # check if the planets are not correct
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"] \
        or planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    # check if the planets are in correct order
    if planet1 < planet2 or (planet1 > planet2 and planet1 not in ["Saturn", "Uranus"]) or \
        (planet1 < planet2 and planet2 not in ["Saturn", "Uranus"]) or \
        (planet1 > planet2 and planet1 not in ["Saturn", "Uranus"]) or \
        (planet1 < planet2 and planet2 not in ["Saturn", "Uranus"]):
        return ()
    
    # check if the planets are in correct order
    if planet1 < planet2:
        # sort the list of planets
        planets = [planet1, planet2]
    else:
        planets = [planet2, planet1]
    # sort the planets by their distance to the sun
    planets = sorted(planets, key=lambda planet: (astronomical.distance(planet, "Sun") - astronomical.distance("Sun", "Sun")))
    # return the sorted list
    return planets
