
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
    solar_system = {"Mercury":0, "Venus":200, "Earth":300, "Mars":400, "Jupiter":500, "Saturn":600, "Uranus":700, "Neptune":800}
    
    if (planet1 not in solar_system) or (planet2 not in solar_system):
        return ()
    
    else:
        planet1_orb = solar_system[planet1]
        planet2_orb = solar_system[planet2]
        
        if planet1_orb < planet2_orb:
            return tuple(planet for planet, orb in solar_system.items() if planet1_orb < orb < planet2_orb)
        else:
            return tuple(planet for planet, orb in solar_system.items() if planet2_orb < orb < planet1_orb)
        


