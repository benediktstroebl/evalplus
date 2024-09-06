
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
    # Hint: You might want to say which planet is bigger or smaller than the Moon.

    plants = {"Mercury": "Jupiter", "Venus": "Earth", "Earth": "Mars", 
              "Mars": "Saturn", "Jupiter": "Uranus", "Saturn": "Neptune", 
              "Uranus": "Neptune", "Neptune": "Pluto"}
    
    if planet1 not in plants.keys() or planet2 not in plants.keys():
        return tuple()
    
    planet1_orbit = plants[planet1]
    planet2_orbit = plants[planet2]
    
    if planet1_orbit == planet2_orbit:
        return tuple()
    
    if plants[planet1_orbit] < plants[planet2_orbit]:
        planet1_orbit, planet2_orbit = planet2_orbit, planet1_orbit
        
    # Now we know that planets are in different orbits.
    
    planet = plants[planet1_orbit]
    
    while planet != planet2_orbit:
        planet = plants[planet]
        
    # Now we have found the shortest orbit between the two planets.
    
    return (planet, )

