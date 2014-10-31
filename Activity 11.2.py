__author__ = 'Derek'

transcript = {'Fall 2013': [['MATH', '151', '01', 'Calculus 1'],
                            ['CHEM', '105', '03', 'General Chemistry'],
                            ['ENGL', '101', '02', 'Writing 1'],
                            ['ENGR', '101', '01', 'Introduction to Engineering'],
                            ['ENGR', '102', '05', 'Computer Aided Design']],

              'Spring 2014': [['ENGR', '112', '02', 'Exploration in Ceramic Engr'],
                              ['ENGR', '113', '01', 'Eplorations-Renewable Energy'],
                              ['MATH', '152', '04', 'Calculus 2'],
                              ['PHED', '118', '01', 'Weight Training'],
                              ['PSYC', '101', '03', 'Introduction to Psychology'],
                              ['VARS', '106', '01', 'Varsity Sport: Lacrosse']],

              'Fall 2014': [['CSCI', '156', '01', 'Computer Science 1'],
                            ['ENGR', '102', '01', 'Computer Aided Design'],
                            ['MATH', '253', '02', 'Calculus 3'],
                            ['PHYS', '125', '01', 'Physics 1'],
                            ['RNEW', '201', '01', 'Renewable Energy']]}

for s in transcript:
    for c in transcript[s]:
        print(s,c)
