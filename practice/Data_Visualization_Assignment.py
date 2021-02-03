import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

interest_data = pd.read_csv(filepath_or_buffer='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/Topic_Survey_Assignment.csv')

interest_data.sort_values(by='Very interested', inplace=True, ascending=False)
interest_data_p = (interest_data / 2233)
axes = interest_data_p.plot(kind='bar', figsize=(20, 8), rot=90, width=0.8, color=('#5cb85c','#5bc0de', '#d9534f'), fontsize=14)
axes.set_title("Percentage of Respondents' Interest in Data Science", fontsize = 16)
axes.legend(fontsize=14)
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
axes.spines['left'].set_visible(False)

for p in axes.patches:
    print(p)
    axes.annotate( "{:,.2%}".format( p.get_height()), xy=(p.get_x() + 0.02, p.get_height() + 0.01) )