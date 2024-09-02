
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

    if not planet1 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    if not planet2 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()

    # find the distance between the orbits of planet1 and planet2
    d1, d2 = planemo.separation(planet1, planet2)
    
    # find the average distance of all planets whose orbit is between the orbit of planet1 and the orbit of planet2
    d_average = d1 + d2 / 2
    
    # find the closest planet to the orbit of planet1 and the orbit of planet2
    closest_planet = planemo.closest(d1, d2)

    if closest_planet == "Mercury":
        closest_planet = planemo.closest(d1, d2 - d1)
    elif closest_planet == "Venus":
        closest_planet = planemo.closest(d1, d2 - d1 - d2)
    elif closest_planet == "Earth":
        closest_planet = planemo.closest(d1, d2 - d1 - d2 - d1)
    elif closest_planet == "Mars":
        closest_planet = planemo.closest(d1, d2 - d1 - d2 - d1 - d2)
    elif closest_planet == "Jupiter":
        closest_planet = planemo.closest(d1, d2 - d1 - d2 - d1 - d2 - d1)
    elif closest_planet == "Saturn":
        closest_planet = planemo.closest(d1, d2 - d1 - d2 - d1 - d2 - d1 - d2)
    elif closest_planet == "Uranus":
        closest_planet = planemo.closest(d1, d2 - d1 - d2
