#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 21:06:21 2022

@author: carrie
"""

import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn import datasets

import warnings
warnings.filterwarnings("ignore")

####### Load Dataset #####################

file = pd.read_csv(r"/Users/carrie/Downloads/Data/bank_loans_clean_with_encoding.csv")

########################################################
st.set_page_config(layout="wide")

st.markdown("## Bank Loan Dataset Analysis")   ## Main Title

################# Hexbin Chart between interest rate & loan amount #################
hexbin_fig = plt.figure(figsize=(15,5))

hexbin_ax = hexbin_fig.add_subplot(111)

file.plot.hexbin(x="Interest Rate", y="Loan Amount",
                             reduce_C_function=np.mean,
                             gridsize=25,
                             #cmap="Greens",
                             ax=hexbin_ax,
                             title="Concentration of Measurements"
                            );


################# line chart between line chart & interest rate#################

record_interest=file.groupby('Public Record')['Interest Rate'].agg(['mean']).reset_index()

line_chart = plt.figure(figsize=(15,5))
plt.plot(record_interest['Public Record'], record_interest['mean'])  

plt.title('Interest rate according to public record', fontweight='bold')
plt.xlabel('Number of public record', fontweight='bold')
plt.ylabel('Interest rate', fontweight='bold')

################# Bar Chart: interest rate per public record#################
avg_file = pd.pivot_table(file, values = 'Interest Rate',  index = 'Public Record', columns = 'Grade')

grade_measurements = avg_file.columns.tolist()

st.sidebar.markdown("### Bar Chart: interest rate per public record : ")

#label => table title, options => lists of options to choose from 
bar_axis = st.sidebar.multiselect(label="interest rate per public record",
                                  options=grade_measurements,
                                  default=['B','C','E'])

# If chose something
if bar_axis:
    bar_fig1 = plt.figure(figsize=(15,5))

    bar_ax = bar_fig1.add_subplot(111)

    sub_avg_file = avg_file[bar_axis]

    sub_avg_file.plot.bar(alpha=0.8, ax=bar_ax, title="interest rate per public record")
    
# default shown 
else:
    bar_fig1 = plt.figure(figsize=(6,4))

    bar_ax = bar_fig1.add_subplot(111)

    sub_avg_file = avg_file[["Interest Rate","Public Record"]]

    sub_avg_file.plot.bar(alpha=0.8, ax=bar_ax, title="interest rate per public record");

################# Bar Chart: loan amount per public record#################
amount_avg_file = pd.pivot_table(file, values = 'Funded Amount', index = 'Public Record', columns = 'Grade')

grade_measurements = amount_avg_file.columns.tolist()

st.sidebar.markdown("### Bar Chart: loan amount per public record : ")

#label => table title, options => lists of options to choose from 
bar_axis = st.sidebar.multiselect(label="funded amount per public record",
                                  options=grade_measurements,
                                  default=['A','B','C','F'])

# If chose something
if bar_axis:
    bar_fig2 = plt.figure(figsize=(15,5))

    bar_ax = bar_fig2.add_subplot(111)

    sub_avg_file = avg_file[bar_axis]

    sub_avg_file.plot.bar(alpha=0.8, ax=bar_ax, title="loan amount per public record")
    
# default shown 
else:
    bar_fig2 = plt.figure(figsize=(6,4))

    bar_ax = bar_fig2.add_subplot(111)

    sub_avg_file = avg_file[["Loan Amount","Public Record"]]

    sub_avg_file.plot.bar(alpha=0.8, ax=bar_ax, title="loan amount per public record");

##################### Layout Application ##################


container1 = st.container()
col1, col2 = st.columns(2)

with container1:
    with col1:
        hexbin_fig
    with col2:
        line_chart
        
container2 = st.container()
col3, col4 = st.columns(2)

with container2:
    with col3:
        bar_fig1
    with col4:
        bar_fig2