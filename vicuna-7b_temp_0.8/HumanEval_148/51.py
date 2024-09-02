
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
    if not isinstance(planet1,str) or not isinstance(planet2,str):
        return ()
    if planet1 not in ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']:
        return ()
    if planet2 not in ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']:
        return ()
    
    def orbits(p1,p2):
        planet1_semi_major_axis =astronomical_unit(p1)
        planet2_semi_major_axis =astronomical_unit(p2)
        planet1_distance_from_sun =astronomical_unit(planet1)
        planet2_distance_from_sun =astronomical_unit(planet2)
        orbit1 =Astronomical_Orbit(planet1_semi_major_axis,planet1_distance_from_sun)
        orbit2 =Astronomical_Orbit(planet2_semi_major_axis,planet2_distance_from_sun)
        planet_list = [(orbit1.asteroid_barycenter.x,orbit1.asteroid_barycenter.y,orbit1.asteroid_barycenter.z),(orbit2.asteroid_barycenter.x,orbit2.asteroid_barycenter.y,orbit2.asteroid_barycenter.z)]
        return planet_list

    planet_list = orbits(planet1, planet2)
    sorted_planet_list = sorted(planet_list, key=lambda x: (astronomical_unit(x[0]), x[1]))
    return sorted_planet_list
