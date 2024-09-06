
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

    
    def orbit_distance(planet1, planet2):
        '''
        It takes two planet names as strings planet1 and planet2. 
        The function should return a tuple containing the distances to the 
        Sun in the respective order of planet1 and planet2.
        Examples
        orbit_distance("Jupiter", "Neptune") ==> (9.5, 10.5)
        orbit_distance("Earth", "Mercury") ==> (9.5, 8.5)
        orbit_distance("Mercury", "Uranus") ==> (8.5, 7.5)
        '''
        
        def distance(x, y):
            '''
            The function takes two planets names as strings planet1 and planet2. 
            The function should return a tuple containing the distances to the 
            Sun in the respective order of planet1 and planet2.
            Examples
            distance("Jupiter", "Neptune") ==> (9.5, 10.5)
            distance("Earth", "Mercury") ==> (9.5, 8.5)
            distance("Mercury",
