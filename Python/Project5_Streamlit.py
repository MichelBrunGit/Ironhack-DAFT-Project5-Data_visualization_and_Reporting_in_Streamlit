#To run Streamlit : Go on Anaconda prompt command and enter ->
# streamlit run C:\Users\Michel\git2\Ironhack-DAFT-Project5-Data_visualization_and_Reporting_in_Streamlit\Python\Project5_Streamlit.py

#import libraries

import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn import datasets

import warnings
import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn import datasets

import warnings
warnings.filterwarnings("ignore")

####### Load Dataset #####################

##Exporting File after encoding
file = pd.read_csv(r"C:\Users\Michel\git2\Ironhack-DAFT-Project5-Data_visualization_and_Reporting_in_Streamlit\data\bank_loans_clean_with_encoding.csv")

# breast_cancer = datasets.load_breast_cancer(as_frame=True)
# breast_cancer_df = pd.concat((breast_cancer["data"], breast_cancer["target"]), axis=1)
# breast_cancer_df["target"] = [breast_cancer.target_names[val] for val in breast_cancer_df["target"]]
########################################################

st.set_page_config(layout="wide")

st.markdown("## Bank Loan Analysis")   ## Main Title


################# Scatter Chart Logic #################

st.sidebar.markdown("### Scatter Chart: Explore Relationship among Grades :")

measurements = ["Loan Amount","Funded Amount","Funded Amount Investor","Term","Interest Rate","Employment Duration","Inquires - six months",
                "Open Account","Public Record","Revolving Balance","Total Accounts","Total Received Interest",
                "Total Received Late Fee","Recoveries","Collection Recovery Fee","Total Current Balance","Total Revolving Credit Limit"]
#measurements = breast_cancer_df.drop(labels=["ID","Grade","Sub Grade","Employment Duration", "Verification Status",
                                             #"Payment Plan","Loan Title","Initial List Status","Application Type"], axis=1).columns.tolist()
# ID,Loan Amount,Funded Amount,Funded Amount Investor,Term,Interest Rate,Grade,Sub Grade,Employment Duration,Home Ownership,Verification Status,
# Loan Title,Debit to Income,Delinquency - two years,Inquires - six months,Open Account,Public Record,Revolving Balance,Revolving Utilities,
# Total Accounts,Initial List Status,Total Received Interest,Total Received Late Fee,Recoveries,Collection Recovery Fee,
# Collection 12 months Medical,Application Type,Last week Pay,Total Collection Amount,Total Current Balance,Total Revolving Credit Limit,
# Loan Status,Grade_enc,Sub Grade_enc,Employment Duration_enc,Verification Status_enc,Loan Title_enc,Initial List Status_enc,Application Type_enc
x_axis = st.sidebar.selectbox("X-Axis", measurements)
y_axis = st.sidebar.selectbox("Y-Axis", measurements, index=1)
grade = st.sidebar.selectbox("Grade", sorted(file["Grade"].unique()))

if x_axis and y_axis:
    scatter_fig = plt.figure(figsize=(6,4))

    scatter_ax = scatter_fig.add_subplot(111)

    malignant_df = file[file["Grade"] == "A"]
    benign_df = file[file["Grade"] == grade]

    benign_df.plot.scatter(x=x_axis, y=y_axis, s=120, c="dodgerblue", alpha=0.6, ax=scatter_ax,
                           title="{} vs {}".format(x_axis.capitalize(), y_axis.capitalize()), label=grade);


########## Bar Chart Logic ##################

st.sidebar.markdown("### Bar Chart: Average Data per Loan Title : ")
default2 = ["Loan Amount","Funded Amount","Funded Amount Investor"]
title2="Average Data per Loan Title"
avg_breast_cancer_df2 = file.groupby("Loan Title").mean()
bar_axis2 = st.sidebar.multiselect(label=title2,
                                  options=measurements,
                                  default=default2)

if bar_axis2:
    bar_fig2 = plt.figure(figsize=(6,4))

    bar_ax2 = bar_fig2.add_subplot(111)

    sub_avg_breast_cancer_df2 = avg_breast_cancer_df2[bar_axis2]

    sub_avg_breast_cancer_df2.plot.bar(alpha=0.8, ax=bar_ax2, title=title2);

else:
    bar_fig2 = plt.figure(figsize=(6,4))

    bar_ax2 = bar_fig2.add_subplot(111)

    sub_avg_breast_cancer_df2 = avg_breast_cancer_df2[default2]

    sub_avg_breast_cancer_df2.plot.bar(alpha=0.8, ax=bar_ax2, title=title2);

########## Bar Chart Logic ##################

st.sidebar.markdown("### Bar Chart: Average Data per Grade : ")
default1 = ["Loan Amount","Funded Amount","Funded Amount Investor"]
title1="Average Data per Grade"
avg_breast_cancer_df = file.groupby("Grade").mean()
bar_axis = st.sidebar.multiselect(label=title1,
                                  options=measurements,
                                  default=default1)

if bar_axis:
    bar_fig = plt.figure(figsize=(6,4))

    bar_ax = bar_fig.add_subplot(111)

    sub_avg_breast_cancer_df = avg_breast_cancer_df[bar_axis]

    sub_avg_breast_cancer_df.plot.bar(alpha=0.8, ax=bar_ax, title=title1);

else:
    bar_fig = plt.figure(figsize=(6,4))

    bar_ax = bar_fig.add_subplot(111)

    sub_avg_breast_cancer_df = avg_breast_cancer_df[default1]

    sub_avg_breast_cancer_df.plot.bar(alpha=0.8, ax=bar_ax, title=title1);

########## Bar Chart Logic ##################

st.sidebar.markdown("### Bar Chart: Average Data per Sub Grade : ")
default3 = ["Loan Amount","Funded Amount","Funded Amount Investor"]
title3="Average Data per Sub Grade"
avg_breast_cancer_df3 = file.groupby("Sub Grade").mean()
bar_axis3 = st.sidebar.multiselect(label=title3,
                                  options=measurements,
                                  default=default3)

if bar_axis3:
    bar_fig3 = plt.figure(figsize=(6,4))

    bar_ax3 = bar_fig3.add_subplot(111)

    sub_avg_breast_cancer_df3 = avg_breast_cancer_df3[bar_axis3]

    sub_avg_breast_cancer_df3.plot.bar(alpha=0.8, ax=bar_ax3, title=title3);

else:
    bar_fig3 = plt.figure(figsize=(6,4))

    bar_ax3 = bar_fig3.add_subplot(111)

    sub_avg_breast_cancer_df3 = avg_breast_cancer_df3[default3]

    sub_avg_breast_cancer_df3.plot.bar(alpha=0.8, ax=bar_ax3, title=title3);
#
#
# ################# Histogram Logic ########################
#
# st.sidebar.markdown("### Histogram: Explore Distribution of Measurements : ")
#
# hist_axis = st.sidebar.multiselect(label="Histogram Ingredient", options=measurements, default=["mean radius", "mean texture"])
# bins = st.sidebar.radio(label="Bins :", options=[10,20,30,40,50], index=4)
#
# if hist_axis:
#     hist_fig = plt.figure(figsize=(6,4))
#
#     hist_ax = hist_fig.add_subplot(111)
#
#     sub_breast_cancer_df = breast_cancer_df[hist_axis]
#
#     sub_breast_cancer_df.plot.hist(bins=bins, alpha=0.7, ax=hist_ax, title="Distribution of Measurements");
# else:
#     hist_fig = plt.figure(figsize=(6,4))
#
#     hist_ax = hist_fig.add_subplot(111)
#
#     sub_breast_cancer_df = breast_cancer_df[["mean radius", "mean texture"]]
#
#     sub_breast_cancer_df.plot.hist(bins=bins, alpha=0.7, ax=hist_ax, title="Distribution of Measurements");
#
# #################### Hexbin Chart Logic ##################################
#
# st.sidebar.markdown("### Hexbin Chart: Explore Concentration of Measurements :")
#
# hexbin_x_axis = st.sidebar.selectbox("Hexbin-X-Axis", measurements, index=0)
# hexbin_y_axis = st.sidebar.selectbox("Hexbin-Y-Axis", measurements, index=1)
#
# if hexbin_x_axis and hexbin_y_axis:
#     hexbin_fig = plt.figure(figsize=(6,4))
#
#     hexbin_ax = hexbin_fig.add_subplot(111)
#
#     breast_cancer_df.plot.hexbin(x=hexbin_x_axis, y=hexbin_y_axis,
#                                  reduce_C_function=np.mean,
#                                  gridsize=25,
#                                  #cmap="Greens",
#                                  ax=hexbin_ax, title="Concentration of Measurements");

################# Hexbin Chart between interest rate & loan amount #################
hexbin_fig = plt.figure(figsize=(6, 4))

hexbin_ax = hexbin_fig.add_subplot(111)

file.plot.hexbin(x="Interest Rate", y="Loan Amount",
                 reduce_C_function=np.mean,
                 gridsize=25,
                 # cmap="Greens",
                 ax=hexbin_ax,
                 title="Concentration of Measurements"
                 );

################# line chart between line chart & interest rate#################

record_interest = file.groupby('Public Record')['Interest Rate'].agg(['mean']).reset_index()

line_chart = plt.figure(figsize=(6, 4))
plt.plot(record_interest['Public Record'], record_interest['mean'])

plt.title('Interest rate according to public record', fontweight='bold')
plt.xlabel('Number of public record', fontweight='bold')
plt.ylabel('Interest rate', fontweight='bold')

################# Bar Chart: interest rate per public record#################
avg_file = pd.pivot_table(file, values='Interest Rate', index='Public Record', columns='Grade')

grade_measurements = avg_file.columns.tolist()

st.sidebar.markdown("### Bar Chart: interest rate per public record : ")

# label => table title, options => lists of options to choose from
bar_axis5 = st.sidebar.multiselect(label="Interest rate per public record",
                                  options=grade_measurements,
                                  default=['B', 'C', 'E'])

# If chose something
if bar_axis5:
    bar_fig5 = plt.figure(figsize=(6, 4))

    bar_ax5 = bar_fig5.add_subplot(111)

    sub_avg_file5 = avg_file[bar_axis5]

    sub_avg_file5.plot.bar(alpha=0.8, ax=bar_ax5, title="Interest rate per public record")

# default shown
else:
    bar_fig5 = plt.figure(figsize=(6, 4))

    bar_ax5 = bar_fig5.add_subplot(111)

    sub_avg_file5 = avg_file[["Interest Rate", "Public Record"]]

    sub_avg_file5.plot.bar(alpha=0.8, ax=bar_ax5, title="Interest rate per public record");

################# Bar Chart: loan amount per public record#################
amount_avg_file6 = pd.pivot_table(file, values='Funded Amount', index='Public Record', columns='Grade')

grade_measurements6 = amount_avg_file6.columns.tolist()

st.sidebar.markdown("### Bar Chart: loan amount per public record : ")

# label => table title, options => lists of options to choose from
bar_axis6 = st.sidebar.multiselect(label="funded amount per public record",
                                  options=grade_measurements,
                                  default=['A', 'B', 'C', 'F'])

# If chose something
if bar_axis:
    bar_fig6 = plt.figure(figsize=(6, 4))

    bar_ax6 = bar_fig6.add_subplot(111)

    sub_avg_file6 = avg_file[bar_axis6]

    sub_avg_file6.plot.bar(alpha=0.8, ax=bar_ax6, title="Loan amount per public record")

# default shown
else:
    bar_fig6 = plt.figure(figsize=(6, 4))

    bar_ax6 = bar_fig6.add_subplot(111)

    sub_avg_file6 = avg_file[["Loan Amount", "Public Record"]]

    sub_avg_file6.plot.bar(alpha=0.8, ax=bar_ax6, title="Loan amount per public record");

##################### Layout Application ##################

container1 = st.container()
col1, col2 = st.columns(2)

with container1:
    with col1:
        scatter_fig
    with col2:
        bar_fig2

container2 = st.container()
col3, col4 = st.columns(2)

with container2:
    with col3:
        bar_fig
    with col4:
        bar_fig3

container3 = st.container()
col5, col6 = st.columns(2)

with container3:
    with col5:
        hexbin_fig
    with col6:
        line_chart

container4 = st.container()
col7, col8 = st.columns(2)

with container4:
    with col7:
        bar_fig5
    with col8:
        bar_fig6




# #col3, col4 = st.columns(2)
#
# with container2:
#     with col3:
#         #hist_fig
#     with col4:
        #hexbin_fig

