import pandas as pd

# read the CSV files into dataframes
buyers_df = pd.read_csv('buyers_example.csv')
bookings_df = pd.read_csv('bookings_example.csv')

# merge the dataframes on the name and contact and email column
merged_df = pd.merge(buyers_df, bookings_df, on=['name', 'contact', 'email'])

# group by name, contact and email and count the number of bookings for each buyer
booking_counts = merged_df.groupby(['name', 'contact', 'email']).size()

# find buyers who booked more than they purchased
overbookers = booking_counts[booking_counts > 1]

# convert overbookers Series back to DataFrame
overbookers_df = overbookers.reset_index()

# rename the 0 column to 'count'
overbookers_df = overbookers_df.rename(columns={0: 'count'})

# write the overbookers dataframe to a new CSV file
overbookers_df.to_csv('overbookers.csv', index=False)
