
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
    '''
    planets = ["Jupiter", "Neptune", "Moon", "Mars", "Mercury", "Venus", "Earth", "Saturn", "Uranus", "Pluto"]
    sun = "Sun"
    planets.remove(planet1)
    planets.remove(planet2)
    planets.append(sun)
    
    planet1_orbit = planets.index(planet1)
    planet2_orbit = planets.index(planet2)
    
    if planet2_orbit > planet1_orbit:
        #if planet2 is higher we go to the higher index
        for i in range(planet1_orbit, planet2_orbit):
            #bottom and top elements at the begin and end
            if i == planet1_orbit or i == planet2_orbit:
                continue
            if planets[i] == sun:
                break
            result.append(planets[i])
            
    else:
        #if planet1 is higher we go to the lower index
        for i in range(planet2_orbit, planet1_orbit):
            if i == planet2_orbit or i == planet1_orbit:
                continue
            if planets[i] == sun:
                break
            result.append(planets[i])
          
    #we make a new string with , between each element     
    return tuple(result)
    '''
    # shorter version
    return tuple(sorted(set([x for x in set([planet1, planet2]) if x != sun and (planet1_orbit < planets.index(x) < planet2_orbit)])))
