******************************************
****    WEATHER REPORT ACQUISITION    ****
******************************************


***************
* INSTALLS:
***************

    - VSCode
    - Python3

    *************pip install pyperclip (for copy/paste of location into google earth)
    *************pip install pyautogui (for copy/paste of location into google earth)

***************
* API KEY:
***************

    Make sure to update the API key to the company's or current user's api key

    Website to access key: https://www.visualcrossing.com/sign-up

INPUT:

    Date - use yyyy-mm-dd format (with dashes)
    Time - use 24 hr time in HH:MM:SS format (with colons; put 00 for seconds)
    UTC Offset - use timezone offset of given location *AT DOL* (account for Daylight Savings)
        Standard Offsets: 
                            MDT (spring/summer)  = -6
                            MST (fall/winter)    = -7

                            Arizona (year-round) = -7

                            CDT (spring/summer)  = -5
                            CST (fall/winter)    = -6

                            PDT (spring/summer)  = -7
                            PST (fall/winter)    = -8
    Latitude - use decimal format (up to 5 deicmal places)
    Longitude - use decimal format (up to 5 decimal places)


OUTPUT:

    Text file with relevant data needed for CA reports or 3D simulations (FARO).

    Values:

        Cloud Cover - percentage (0-100%)
        Visibility - perceived distance in daylight (miles)
            Accounts for haze, mist, fog, or smoke
        Precipitation - fallen precipitation (inches)
            Snow Depth - average amount of snow currently on the ground (inches)
        Windspeed - average speed for two minutes prior to measurement (mph)
        Moonphase - decimal value (0-1) representing current phase
            - 0 – new moon
            - 0-0.25 – waxing crescent
            - 0.25 – first quarter
            - 0.25-0.5 – waxing gibbous
            - 0.5 – full moon
            - 0.5-0.75 – waning gibbous
            - 0.75 – last quarter
            - 0.75 -1 – waning crescent
        Solar Elevation - degrees above the horizon (accounting for elevation)
        Solar Aziumuth - degrees clockwise from true north         

        See detailed information about every datapoint value here:
            https://www.visualcrossing.com/resources/documentation/weather-data/weather-data-documentation/


DOCUMENTATION:

    Virtual Crossing (Weather): 
        https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/

    VC Query Builder (to add explore additional parameters): 
        https://www.visualcrossing.com/weather/weather-data-services#


    EPA Weather Service Solar Calculator: 
        https://qed.epa.gov/hms/api_doc/


    pyautogui
        https://pyautogui.readthedocs.org/en/latest/
