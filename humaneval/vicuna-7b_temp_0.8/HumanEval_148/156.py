
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
    
    if planet1 in ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]:
        planet1 = [i.strip() for i in planet1.split(",")]
    elif planet1 in ["Venus","Mars","Jupiter","Saturn","Uranus","Neptune"]:
        planet1 = [i.strip() for i in planet1.split(",")]
    else:
        return ()
    
    if planet2 in ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]:
        planet2 = [i.strip() for i in planet2.split(",")]
    elif planet2 in ["Venus","Mars","Jupiter","Saturn","Uranus","Neptune"]:
        planet2 = [i.strip() for i in planet2.split(",")]
    else:
        return ()
    
    if planet1[0]==planet2[0]:
        planets = sorted([planet,i[0] for planet,i in
                         [(planet1,planet1[0]),(planet2,planet2[0]),(planet1[1:],planet2[1:])]])
    else:
        planets = sorted([planet1,planet2[1:],i[0] for planet,i in
                         [(planet1,planet1[0]),(planet2,planet2[0]),(planet1[1:],planet2)]])
    
    return planets

planets = bf("Venus", "Earth")
