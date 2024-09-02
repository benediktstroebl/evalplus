
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

    
    def get_orbits(planet):
        if planet == "Mercury": return (3.3, "Venus")
        elif planet == "Venus": return (6.5, "Earth")
        elif planet == "Earth": return (9.5, "Mars")
        elif planet == "Mars": return (10.9, "Jupiter")
        elif planet == "Jupiter": return (11.8, "Saturn")
        elif planet == "Saturn": return (12.1, "Uranus")
        elif planet == "Uranus": return (18.1, "Neptune")
        elif planet == "Neptune": return (30.7, "Sun")
        else: return ()

    def get_dist(orbits, planet1, planet2):
        dist = 0
        for orbit in orbits:
            if planet1 in orbit and planet2 in orbit:
                dist = orbit[0] - orbit[1]
                break
        return dist

    if planet1 == "" or planet2 == "":
        return ()
    else
