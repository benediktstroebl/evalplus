
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
    if planet1 not in PLANETS or planet2 not in PLANETS:
        return ()
    if planet1 == planet2:
        return ()
    
    planet1_sun, planet2_sun = PLANETS[planet1], PLANETS[planet2]
    planet1_sun_dist = distance(planet1_sun, planet1_sun)
    planet2_sun_dist = distance(planet2_sun, planet2_sun)
    
    if planet1_sun_dist > planet2_sun_dist:
        planet1_sun, planet2_sun = planet2_sun, planet1_sun
        
    if planet1_sun == planet2_sun:
        return (planet1, planet2)
    
    planet1_orbits = orbit_map[planet1_sun]
    planet2_orbits = orbit_map[planet2_sun]
    
    planet1_orbit = planet1_orbits[-1]
    planet2_orbit = planet2_orbits[-1]
    
    while planet1_orbit != planet2_orbit:
        planet1_orbit = planet1_orbits.pop()
        planet2_orbit = planet2_orbits.pop()
        if planet1_orbit not in planet2_orbits:
            planet1_orbits.append(planet1_orbit)
        if planet2_orbit not in planet1_orbits:
            planet2_orbits.append(planet2_orbit)
        
    orbits = sorted([planet1] + planet1_orbits + [planet2] + planet2_orbits, 
                    key=lambda moon: distance(PLANETS[planet1], PLANETS[moon]))
    
    return tuple(orbits)
