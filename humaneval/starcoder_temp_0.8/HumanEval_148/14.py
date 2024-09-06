
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
    
    pl_dict = {
        "Mercury" : 0.387,
        "Venus" : 0.723,
        "Earth" : 1.0,
        "Mars" : 1.524,
        "Jupiter" : 5.203,
        "Saturn" : 9.539,
        "Uranus" : 19.18,
        "Neptune" : 30.06,
    }
    
    pl_list = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]
    
    pl_1_idx = pl_list.index(planet1)
    pl_2_idx = pl_list.index(planet2)
    
    ans = []
    for i in range(pl_1_idx, pl_2_idx + 1):
        ans.append(pl_list[i])
    
    return tuple(ans)
