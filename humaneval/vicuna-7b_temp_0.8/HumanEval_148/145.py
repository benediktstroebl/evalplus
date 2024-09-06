
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
    # check for correct planet names
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    
    # create empty list for sorted planets
    sorted_planets = []
    
    # check for proximity of planet1 and planet2
    if planet1 < planet2:
        # check for inner planets
        if planet1 < "Mercury":
            sorted_planets.append(planet1)
            sorted_planets.append(planet2)
            sorted_planets.sort(key=lambda x: (x > "Mercury"), reverse=True)
        # check for outer planets
        elif "Jupiter" <= planet1:
            sorted_planets.append(planet1)
            sorted_planets.append(planet2)
            sorted_planets.sort(key=lambda x: (x > "Jupiter"), reverse=True)
    else:
        # check for inner planets
        if planet2 < "Mercury":
            sorted_planets.append(planet2)
            sorted_planets.append(planet1)
            sorted_planets.sort(key=lambda x: (x > "Mercury"), reverse=True)
        # check for outer planets
        elif "Jupiter" <= planet2:
            sorted_planets.append(planet2)
            sorted_planets.append(planet1)
            sorted_planets.sort(key=lambda x: (x > "Jupiter"), reverse=True)
    return sorted_planets
