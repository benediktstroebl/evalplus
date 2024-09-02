
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

    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    try:
        if planet1 in planets and planet2 in planets:
            planets_list = []
            for i in range(len(planets)):
                if planets[i] == planet1 or planets[i] == planet2:
                    planets_list.append(planets[i])
            for i in range(len(planets)):
                if planets[i] == planet2:
                    for j in range(len(planets)):
                        if planets[j] == planet1:
                            if planets[j] < planets[i] or planets[j] == planets[i]:
                                planets_list.append(planets[j])
            return tuple(planets_list)
    except:
        return ()
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
