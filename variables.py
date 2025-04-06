
# ### Absorption

# absorption (A, O)
absorption_rates = {
    'Atlanta': (-0.022588977749568005, -0.00732961656528534),
    'Austin': (-0.053831439593598505, -0.026366892164422204),
    'Baltimore': (-0.014402099922755261, -0.005147754659864611), 
    'Boston': (-0.029969134164771902, -0.011081917032427216),
    'Charlotte': (-0.029097258685895997, -0.034973901999187214),
    'Chicago': (-0.028978654311836275, -0.03531692861556808),  
    'Chicago Suburbs': (-0.009359460176861338, 0.0009917111992323018), 
    'Dallas/Ft Worth': (-0.009950265078867248, -0.0026829764313393584),
    'Denver':  (-0.030744320256725036, -0.019115843962804146),  
    'Detroit': (-0.014402099922755261, -0.005147754659864611), 
    'Houston': (-0.0033821995029679262, -0.0009973758041107166),
    'Los Angeles': (-0.024518875716068075, -0.01301887242119987),
    'Manhattan': (-0.02010481058626688, -0.03209074988074955),
    'Nashville': (-0.027813898586050868, -0.02360324645464407),
    'Northern New Jersey': (-0.004553724270000923, 0.010556213549418455),
    'Northern Virginia': (-0.009088414839254471, 0.0010518660979513053),
    'Orange County': (-0.009838022065392011, -0.007423543101770445),
    'Philadelphia': (-0.01824711379288069, -0.004704105034526766),
    'Phoenix': (-0.0246509729805061, 0.0005434075531365124),
    'Raleigh/Durham': (-0.03249189391395942, -0.0035755733395049882),
    'Salt Lake City': (-0.042753829685275434, -0.02923822771966973),
    'San Diego': (-0.018787468581848914, -0.0006801506864007474),
    'San Francisco': (-0.07203686728867384, -0.07698653830148533),
    'Seattle': (-0.04447649820603075, -0.025559230697896996),
    'South Bay/San Jose': (-0.037018952994871526, -0.026381363658888376),
    'South Florida': (-0.007124659865635555, 0.002390870201891718),
    'Southern Maryland': (-0.008100961117428517, 0.0011767018414884812),
    'Tampa': (-0.028027310449950927, -0.0028264714609103556),
    'Washington D.C.': (-0.021611869757852228, -0.017655357434349584),
}


# ### Expected Price

# expected price A, 0 = 2025_Q1, Q2, Q3, Q4
expected_rent = {
    'Atlanta': ([35.4, 35.5, 35.6, 35.7], [25.7, 26.0, 26.3, 26.6]),
 'Austin': ([51.3, 51.4, 51.4, 51.5], [34.2, 34.1, 34.0, 33.9]),
 'Baltimore': ([26.5, 26.6, 26.8, 26.9], [21.0, 20.9, 20.9, 20.8]),
 'Boston': ([59.5, 61.2, 62.9, 64.6], [30.9, 30.7, 30.5, 30.3]),
 'Charlotte': ([37.2, 37.6, 38.0, 38.5], [27.8, 27.9, 27.9, 28.0]),
 'Chicago': ([54.1, 54.9, 55.8, 56.7], [38.9, 38.9, 38.9, 38.8]),
 'Chicago Suburbs': ([31.6, 31.9, 32.1, 32.4], [22.8, 22.9, 23.0, 23.1]),
 'Dallas/Ft Worth': ([35.0, 35.3, 35.6, 35.9], [24.5, 24.4, 24.3, 24.2]),
 'Denver': ([41.5, 42.2, 43.0, 43.7], [28.3, 28.1, 28.0, 27.9]),
 'Detroit': ([23.3, 23.1, 22.9, 22.8], [20.0, 20.1, 20.1, 20.1]),
 'Houston': ([36.2, 36.1, 36.0, 36.0], [22.7, 22.6, 22.6, 22.5]),
 'Los Angeles': ([50.3, 50.5, 50.6, 50.8], [40.7, 40.4, 40.2, 39.9]),
 'Manhattan': ([84.8, 84.8, 84.8, 84.8], [60.9, 60.4, 60.0, 59.6]),
 'Nashville': ([40.8, 41.9, 43.1, 44.3], [29.4, 29.4, 29.5, 29.5]),
 'Northern New Jersey': ([32.9, 33.0, 33.0, 33.0], [25.0, 25.2, 25.4, 25.5]),
 'Northern Virginia': ([36.4, 36.4, 36.4, 36.5], [32.6, 32.6, 32.6, 32.7]),
 'Orange County': ([35.6, 35.6, 35.6, 35.6], [30.6, 30.6, 30.6, 30.5]),
 'Philadelphia': ([34.1, 34.2, 34.4, 34.6], [28.7, 29.1, 29.5, 29.9]),
 'Phoenix': ([32.6, 32.7, 32.7, 32.7], [26.9, 27.0, 27.0, 27.0]),
 'Raleigh/Durham': ([30.4, 30.3, 30.3, 30.2], [24.1, 24.1, 24.0, 23.9]),
 'Salt Lake City': ([30.3, 30.4, 30.6, 30.7], [24.3, 24.3, 24.4, 24.4]),
 'San Diego': ([48.4, 49.0, 49.7, 50.3], [33.8, 33.8, 33.8, 33.8]),
 'San Francisco': ([75.5, 75.7, 76.0, 76.2], [55.6, 54.4, 53.3, 52.2]),
 'Seattle': ([49.8, 49.3, 48.7, 48.1], [35.8, 35.9, 35.9, 36.0]),
 'South Bay/San Jose': ([62.7, 62.9, 63.1, 63.4], [56.7, 55.7, 54.8, 53.8]),
 'South Florida': ([56.4, 58.1, 60.0, 61.8], [37.5, 37.9, 38.4, 38.9]),
 'Southern Maryland': ([31.7, 31.4, 31.2, 30.9], [28.8, 28.8, 28.8, 28.8]),
 'Tampa': ([33.0, 33.1, 33.2, 33.2], [25.7, 25.9, 26.1, 26.2]),
 'Washington D.C.': ([58.3, 58.3, 58.4, 58.4], [48.6, 48.6, 48.7, 48.8])}


# ### Rank Industries

market_counts_by_industry = {'Financial Services and Insurance': {'Manhattan': 1400,
  'Atlanta': 199,
  'Dallas/Ft Worth': 190,
  'Chicago': 188,
  'South Florida': 184,
  'Northern New Jersey': 168,
  'Philadelphia': 147,
  'Los Angeles': 133,
  'Northern Virginia': 126,
  'Phoenix': 115,
  'Charlotte': 114,
  'Houston': 111,
  'Denver': 105,
  'Boston': 102,
  'Orange County': 99,
  'Tampa': 99,
  'Chicago Suburbs': 94,
  'San Francisco': 81,
  'Washington D.C.': 79,
  'Southern Maryland': 76,
  'San Diego': 72,
  'Seattle': 69,
  'Austin': 66,
  'Baltimore': 60,
  'Detroit': 58,
  'Raleigh/Durham': 38,
  'South Bay/San Jose': 33,
  'Nashville': 24,
  'Salt Lake City': 23},
 'Technology, Advertising, Media, and Information': {'Manhattan': 868,
  'Northern Virginia': 311,
  'Los Angeles': 246,
  'South Bay/San Jose': 240,
  'San Francisco': 191,
  'Seattle': 149,
  'Atlanta': 147,
  'Chicago': 143,
  'Austin': 136,
  'Washington D.C.': 129,
  'Boston': 129,
  'Denver': 112,
  'Northern New Jersey': 111,
  'Dallas/Ft Worth': 103,
  'Philadelphia': 85,
  'San Diego': 81,
  'Raleigh/Durham': 80,
  'Orange County': 73,
  'South Florida': 72,
  'Houston': 64,
  'Phoenix': 62,
  'Tampa': 52,
  'Southern Maryland': 47,
  'Baltimore': 45,
  'Charlotte': 42,
  'Detroit': 35,
  'Chicago Suburbs': 35,
  'Salt Lake City': 30,
  'Nashville': 17},
 'Legal Services': {'Manhattan': 393,
  'Washington D.C.': 204,
  'Chicago': 148,
  'Los Angeles': 145,
  'Houston': 113,
  'Philadelphia': 111,
  'South Florida': 96,
  'Dallas/Ft Worth': 82,
  'Denver': 71,
  'Atlanta': 70,
  'Northern Virginia': 67,
  'Northern New Jersey': 65,
  'Tampa': 65,
  'San Francisco': 59,
  'Orange County': 45,
  'San Diego': 41,
  'Boston': 40,
  'Austin': 38,
  'Seattle': 38,
  'Detroit': 31,
  'Charlotte': 29,
  'South Bay/San Jose': 29,
  'Raleigh/Durham': 28,
  'Southern Maryland': 27,
  'Baltimore': 24,
  'Phoenix': 22,
  'Nashville': 10,
  'Salt Lake City': 10,
  'Chicago Suburbs': 8}}

# ### Occupancy Rates
occupancy_rates = {'Austin': 0.5170427840526316,
 'Houston': 0.5037726654210527,
 'Dallas/Ft Worth': 0.4857677595789474,
 'Los Angeles': 0.3984061114736842,
 'Chicago': 0.3889468357368421,
 'Washington D.C.': 0.3691180633157895,
 'Philadelphia': 0.36561050910526316,
 'Manhattan': 0.34934319599999997,
 'South Bay/San Jose': 0.31839943989473685,
 'San Francisco': 0.31761341615789473
 }

# ### Best Quarter to Find Space
best_times = {'Atlanta': 'Q1',
 'Austin': 'Q3',
 'Baltimore': 'Q2',
 'Boston': 'Q1',
 'Charlotte': 'Q1',
 'Chicago': 'Q1',
 'Chicago Suburbs': 'Q3',
 'Dallas/Ft Worth': 'Q3',
 'Denver': 'Q1',
 'Detroit': 'Q3',
 'Houston': 'Q1',
 'Los Angeles': 'Q1',
 'Manhattan': 'Q3',
 'Nashville': 'Q1',
 'Northern New Jersey': 'Q1',
 'Northern Virginia': 'Q1',
 'Orange County': 'Q1',
 'Philadelphia': 'Q1',
 'Phoenix': 'Q1',
 'Raleigh/Durham': 'Q1',
 'Salt Lake City': 'Q1',
 'San Diego': 'Q3',
 'San Francisco': 'Q4',
 'Seattle': 'Q3',
 'South Bay/San Jose': 'Q1',
 'South Florida': 'Q1',
 'Southern Maryland': 'Q1',
 'Tampa': 'Q1',
 'Washington D.C.': 'Q1'}


# ### Talent Pool
university_enrollment = {'Atlanta': '  520,034 ',
 'Austin': '  1,530,623 ',
 'Baltimore': '  330,101 ',
 'Boston': '  472,497 ',
 'Charlotte': '  546,045 ',
 'Chicago': '  699,580 ',
 'Chicago Suburbs': '  699,580 ',
 'Dallas/Ft Worth': '  1,530,623 ',
 'Denver': '  325,586 ',
 'Detroit': '  475,669 ',
 'Houston': '  1,530,623 ',
 'Los Angeles': '  2,396,351 ',
 'Manhattan': '  1,121,285 ',
 'Nashville': '  294,994 ',
 'Northern New Jersey': '  363,215 ',
 'Northern Virginia': '  526,470 ',
 'Orange County': '  2,396,351 ',
 'Philadelphia': '  628,647 ',
 'Phoenix': '  563,340 ',
 'Raleigh/Durham': '  546,045 ',
 'Salt Lake City': '  386,226 ',
 'San Diego': '  2,396,351 ',
 'San Francisco': '  2,396,351 ',
 'Seattle': '  315,071 ',
 'South Bay/San Jose': '  2,396,351 ',
 'South Florida': '  934,983 ',
 'Southern Maryland': '  330,101 ',
 'Tampa': '  934,983 ',
 'Washington D.C.': '  122,546 '}


# ### Economic Growth Rate from 2018 to 2023
region_growth_map = {
    "Atlanta": 18364,
    "Austin": 22330,
    "Baltimore": 16037,
    "Boston": 28245,
    "Charlotte": 21810,
    "Chicago": 17449,
    "Chicago Suburbs": 17449,
    "Dallas/Ft Worth": 16024,
    "Denver": 30240,
    "Detroit": 19240,
    "Houston": 14312,
    "Los Angeles": 13200,
    "Manhattan": 17917,
    "Nashville": 31758,
    "Northern New Jersey": 29185,
    "Northern Virginia": 33467,
    "Orange County": 21199,
    "Philadelphia": 23159,
    "Phoenix": 23539,
    "Raleigh/Durham": 27351,
    "Salt Lake City": 20655,
    "San Diego": 11424,
    "San Francisco": 63032,
    "Seattle": 32697,
    "South Bay/San Jose": 80338,
    "South Florida": 41250,
    "Southern Maryland": 16037,
    "Tampa": 20737,
    "Washington D.C.": 12862
}
