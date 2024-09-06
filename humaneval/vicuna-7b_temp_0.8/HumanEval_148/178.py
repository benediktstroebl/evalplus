
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
    if not (planet1 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]):
        return ()
    if not (planet2 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]):
        return ()

    # sort the list of planets by the distance from the sun
    planets = sorted([(_get_distance(planet), planet) for planet in planet1.split(",") + planet2.split(",") if planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]], key=lambda x: x[0])
    
    # check if the orbit of the first planet is between the orbit of the second planet and the sun
    if planet1 in ["Mercury", "Venus"]:
        if not (planets[0][0] < _get_distance(planet2) and _get_distance(planets[0][1]) > _get_distance(planet2)):
            return ()
    elif planet1 == "Earth":
        if not (planets[0][0] < _get_distance(planet2) and _get_distance(planets[1][1]) > _get_distance(planet2)):
            return ()
    elif planet1 in ["Mars", "Jupiter", "Saturn", "Uranus"]:
        if not (planets[1][0] < _get_distance(planet2) and _get_distance(planets[0][1]) > _get_distance(planet2)):
            return ()
    elif planet1 == "Neptune":
        if not (planets[1][0] < _get_distance(planet2) and _get_distance(planets[1][1]) > _get_distance(planet2)):
            return ()
    else:
        return ()
        
