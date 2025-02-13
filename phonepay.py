#importing libraries 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import plotly.express as px

#giving title
st.title("PhonePe Transaction Insights")

#connecting python with mysql
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Sanjana@2003'
)
mycursor = mydb.cursor()


def map_data(year,quarter):
    query = """select state,
                sum(Transaction_Amount) as total_trans_amount
                from aggregated_transaction 
                where year = %s and quater = %s
                group by state
                order by total_trans_amount"""
    mycursor.execute(query,(year,quarter))
    data = mycursor.fetchall() #fetching all the result from sql query
    df = pd.DataFrame(data,columns = ['state','total_trans_amount'])  #creating the dataframe
    return df   #returning the dataframe

def map_state(df):
    maping = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
              "andhra-pradesh":"Andhra Pradesh",
              "arunachal-pradesh":"Arunachal Pradesh",
              "assam":"Assam",
              "bihar":"Bihar",
              "chandigarh":"Chandigarh",
              "chhattisgarh":"Chhattisgarh",
              "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
              "delhi":"Delhi",
              "goa":"Goa",
              "gujarat":"Gujarat",
              "haryana":"Haryana",
              "himachal-pradesh":"Himachal Pradesh",
              "jammu-&-kashmir":"Jammu & Kashmir",
              "jharkhand":"Jharkhand",
              "karnataka":"Karnataka",
              "kerala":"Kerala",
              "ladakh":"Ladakh",
              "madhya-pradesh":"Madhya Pradesh",
              "maharashtra":"Maharashtra",
              "manipur":"Manipur",
              "meghalaya":"Meghalaya",
              "mizoram":"Mizoram",
              "nagaland":"Nagaland",
              "odisha":"Odisha",
              "puducherry":"Puducherry",
              "punjab":"Punjab",
              "rajasthan":"Rajasthan",
              "sikkim":"Sikkim",
              "tamil-nadu":"Tamil Nadu",
              "telangana":"Telangana",
              "tripura":"Tripura",
              "uttar-pradesh":"Uttarakhand",
              "uttarakhand":"Uttar Pradesh",
              "west-bengal":"West Bengal"}
    df['state'] = df['state'].map(maping)
    return df


mycursor.execute("use phonepay")
#creating the sidebar navigation menu
page = st.sidebar.radio('Navigation',['Home','Business Cases'])

#checking the selected option is home or business cases
if page == 'Home':
    #creating the selectbox tabels
    select_options=st.selectbox('Tabels',['Aggregated Transaction','Aggregated Insurance','Aggregated User','Map Transaction','Map User',
                                          'Map Insurance','Top Insurance District','Top Insurance Pincode','Top Transaction District',
                                          'Top Transaction Pincode','Top User Districs','Top User Pincode'])


    if select_options == 'Aggregated Transaction':
        st.markdown('<h1 style = "color:blue;"> AGGREGATED TRANSACTION DATAS </h1>',unsafe_allow_html = True)
        mycursor.execute("select * from aggregated_transaction")
        datas = mycursor.fetchall()
        df = pd.DataFrame(datas, columns = ['State','Year','Quarter','Transaction_Type','Total_no_transactions','Transaction_Amount'])
        st.dataframe(df)

    if select_options == 'Aggregated Insurance':
        st.markdown('<h1 style = "color:red;"> AGGREGATED INSURANCE DATAS </h1>',unsafe_allow_html = True)
        mycursor.execute("select * from aggregated_insurance")
        datas = mycursor.fetchall()
        df = pd.DataFrame(datas, columns = ['State','Year','Quater','Type_payment_category','Insurance_Count','Amount'])
        st.dataframe(df)  

    if select_options == 'Aggregated User':
        st.markdown('<h1 style = "color:red;"> AGGREGATED USER DATAS </h1>',unsafe_allow_html = True)
        mycursor.execute("select * from aggregated_user")
        datas = mycursor.fetchall()
        df = pd.DataFrame(datas, columns = ['State','Year','Quater','Brandname','Reguser_brand','Percntage'])
        st.dataframe(df)      

    if select_options == 'Map Transaction':
        st.markdown('<h1 style = "color:blue;" > MAP TRANSACTION DATAS </h1>',unsafe_allow_html = True)
        mycursor.execute("select * from map_transaction")
        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State','Year','Quater','district_name','Transaction_Count','Transaction_Amount'])
        st.dataframe(df)

    if select_options == 'Map User':
        st.markdown('<h1 style = "color:red;" > MAP USER DATAS </h1>',unsafe_allow_html = True)
        mycursor.execute("select * from map_user")
        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State','Year','Quater','Registereduser','Apps'])
        st.dataframe(df)
    
    if select_options == 'Map Insurance':
        st.markdown('<h1 style = "color:darkviolet;">  MAP INSURANCE DATAS </h1>',unsafe_allow_html=True)
        mycursor.execute("select * from Map_insurance")
        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State','Year','Quater','district_name','Total_no_insurance','Amount'])
        st.dataframe(df)

    if select_options == 'Top Insurance District':
        st.markdown('<h1 style = "color:red;">  TOP INSURANCE DISTRICT DATAS </h1>',unsafe_allow_html=True)
        mycursor.execute("select * from Top_insurance_dist")
        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State','Year','Quater','District_name','Transaction_Count','Transactiom_Amount'])
        st.dataframe(df)

    if select_options == 'Top Insurance Pincode':
        st.markdown('<h1 style = "color:darkblue;">  TOP INSURANCE PINCODE DATAS </h1>',unsafe_allow_html=True)
        mycursor.execute("select * from Top_insurance_pin")
        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State','Year','Quater','pincode','Transaction_Count','Transactiom_Amount'])
        st.dataframe(df)

    if select_options == 'Top Transaction District':
        st.markdown('<h1 style = "color:darkviolet;"> TOP TRANSACTION DISTRICT DATAS </h1>',unsafe_allow_html=True)
        mycursor.execute("select * from Top_transaction_dist")
        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State','Year','Quater','district_name','Total_no_transactions','Transactiom_Amount'])
        st.dataframe(df)

    if select_options == 'Top Transaction Pincode':
        st.markdown('<h1 style = "color:darkred;"> TOP TRANSACTION PINCODE DATAS</h1>',unsafe_allow_html=True)
        mycursor.execute("select * from Top_transaction_pin")
        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State','Year','Quater','pincode','Transaction_Count','Transactiom_Amount'])
        st.dataframe(df)

    if select_options == 'Top User Districs':
        st.markdown('<h1 style = "color:blue;"> TOP USER DISTRICT DATAS </h1>',unsafe_allow_html=True)
        mycursor.execute("select * from Topuserdist")
        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State', 'Year', 'Quater', 'District', 'no_Registeruser'])
        st.dataframe(df)

    if select_options == 'Top User Pincode':
        st.markdown('<h1 style = "color:Red;">  TOP USER PINCODE DATAS </h1>',unsafe_allow_html=True)
        mycursor.execute("select * from Topuserpin")
        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State', 'Year', 'Quater', 'pincode', 'no_Registeruser'])
        st.dataframe(df)

    


if page == 'Business Cases':
    select_options = st.selectbox("select any bussiness case",['Case1','Case2','Case3','Case4','Case5'])


    if select_options == 'Case1':
        st.markdown('<h1 style = color:blue;"> VISUALIZATION OF AGGREGATED TRANSACTION </h1>',unsafe_allow_html = True)
        st.markdown('<h2 style = "color:red;"> Total Transaction Amount Analysis</h2>',unsafe_allow_html = True)
        query1 = """
                select distinct year,quater from aggregated_transaction
                """
        mycursor.execute(query1)
        data1 = mycursor.fetchall()
        df1 = pd.DataFrame(data1,columns=['year','quarter'])

        column1,column2 = st.columns(2)
        with column1:
            yea = st.selectbox('Year',list(df1['year'].unique()))
        with column2:
            qu = st.selectbox('Quater',list(df1['quarter'].unique()))
        

        ma_data = map_data(int(yea),int(qu))
        df = map_state(ma_data)
        
        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='total_trans_amount',
            color_continuous_scale='blues'
        )


        fig.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(fig)


        st.markdown('<h1 style = "color:red;">Payment Method Popularity </h1>',unsafe_allow_html = True)
        mycursor.execute("""
                            select Transaction_Type,
                            sum(Total_no_transactions) as total_tranaction,
                            sum(Transaction_Amount) as total_amount
                            from aggregated_transaction
                            group by Transaction_Type
                            order by total_tranaction desc
                         """)
        data2 = mycursor.fetchall()
        df2 = pd.DataFrame(data2,columns=['Transaction_Type','total_transaction','total_amount'])

        column1,column2=st.columns(2)
        with column1:
            fig1 = px.pie(
                df2,
                names='Transaction_Type',
                values = "total_amount",
                title = "Distribution of Total Transaction Amount",
                hole = 0.4,
                labels = ['Transaction_Type']
            )
            st.plotly_chart(fig1)
            
       
        with column2:
            fig2 = px.pie(
                df2,
                names = "Transaction_Type",
                values = "total_transaction",
                title = "Distribution of Total Transaction Count",
                hole = 0.4,
                labels=['Transaction_Type']
            )

            st.plotly_chart(fig2)


        
        st.markdown('<h1 style = "color:blue;"> Top 10 State Wise Total Transaction Amount </h1>',unsafe_allow_html = True)
        mycursor.execute("""
                         select state,
                         sum(Transaction_Amount) as total_amount
                         from aggregated_transaction
                         group by state
                         order by total_amount desc
                         limit 10""")
        data4 = mycursor.fetchall()
        df4 = pd.DataFrame(data4,columns = ['state','total_amount'])

        fig3 = px.bar(
            df4,
            x = 'state',
            y = 'total_amount',
            text = 'total_amount',
            title = 'Total Transaction Amount by State',
            labels = {'state':'State','total_amount':'Total Amount'}
            
            )
        fig3.update_traces(texttemplate ='%{text:.2s}', textposition = 'outside',marker_color='purple')
        st.plotly_chart(fig3)

        



        st.markdown('<h1 style = "color:red;"> Transactions by State and Payment Category </h1>',unsafe_allow_html = True)
        mycursor.execute("""
                            select state,Transaction_Type,
                            sum(Total_no_transactions) as total_transaction,
                            sum(Transaction_Amount) as total_amount
                            from aggregated_transaction
                            group by state,Transaction_Type
                            order by state,total_transaction
        """)
        data5 = mycursor.fetchall()
        df5 = pd.DataFrame(data5,columns = ['state','Transaction_Type','total_transaction','total_amount'])
        state_options = df5['state'].unique()
        select_state = st.selectbox('Select a state',state_options)
        filtered_df = df5[df5['state'] == select_state]

        fig5 = px.line(
            filtered_df,
            x = 'Transaction_Type',
            y = 'total_amount',
            title = f'Transaction Distribution {select_state.capitalize()}',
            labels = {'Transaction_Type':'Transaction Type','total_amount':'Total Transaction Amount'},
            markers = True
        )
        st.plotly_chart(fig5)

        st.markdown('<h1 style = "color:blue;"> Trend Analysis </h1>',unsafe_allow_html = True)
        mycursor.execute("""
                            select year,quater,
                            sum(Total_no_transactions)  as total_transaction_count,
                            sum(Transaction_Amount) as total_amount
                            from aggregated_transaction
                            group by year,quater
                            order by year,quater
        """)
        data6 = mycursor.fetchall()
        df6 = pd.DataFrame(data6,columns = ['year','quater','total_transaction_count','total_amount'])

        year_option = df6['year'].unique()
        select_year = st.selectbox("Select a Year" , year_option)

        filtered_df6 = df6[df6['year'] == select_year]
        st.subheader(f'Transactions for Year {select_year}')

        plt.figure(figsize = (10,6))
        plt.bar(filtered_df6['quater'].astype(str),filtered_df6['total_amount'],color = 'green',width = 0.5)
        plt.xlabel('Quater')
        plt.ylabel('Total Transaction Amount')
        plt.title(f'Transaction Amount Distribution for {select_year}')
        plt.xticks(rotation = 0)
        
        st.pyplot(plt)

    if select_options == "Case2":
        st.markdown('<h1 style = "color:red";> VISUALIZATION OF AGGREGATED USER </h1>',unsafe_allow_html = True)
        st.markdown('<h2 style = "color:lime";> Trend Analysis </h2>',unsafe_allow_html = True)


        mycursor.execute("""
                            SELECT State,Brandname,
                                SUM(Reguser_brand) AS Total_Registered_Users    
                            FROM aggregated_user 
                            GROUP BY State,Brandname 
                            ORDER BY State,Total_Registered_Users DESC
        """)

        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State','Brandname','Total_Registered_Users'])

        state_options = df['State'].unique()
        select_state = st.selectbox("Select a State",state_options)

        filtered_df = df[df['State']== select_state]
        st.subheader(f'Transaction for State,{select_state}')

        fig = px.bar(
            filtered_df,
            x = 'Brandname',
            y = 'Total_Registered_Users',
            text = 'Total_Registered_Users',
            title = f'Top Brands By Registered User',
            labels = {'Brandname': 'Brand Name','Total_Registered_Users':'Registered User'}
        )
        fig.update_traces(texttemplate = '%{text:.2s}',textposition='outside',marker_color = 'darkviolet')
        st.plotly_chart(fig)

        st.markdown('<h1 style = "color:green;"> YEAR WISE TREND </h1>',unsafe_allow_html = True)
        mycursor.execute("""
                        SELECT Year,Brandname,
                            AVG(Percntage) AS Average_App_Opens_Percentage
                        FROM aggregated_user 
                        GROUP BY Year, Brandname
                        ORDER BY Year, Average_App_Opens_Percentage DESC
        """)
        data1 = mycursor.fetchall()
        df1 = pd.DataFrame(data1,columns=['Year','Brandname','Average_App_Opens_Percentage'])


        year_options = df1['Year'].unique()
        select_year = st.selectbox("Select a Year",year_options)

        filtered_df1 = df1[df1['Year']==select_year]

        fig1 = px.pie(
            filtered_df1,
            names = 'Brandname',
            values = 'Average_App_Opens_Percentage',
            title = f'Distribution of Brand Use in {select_year}',
            labels={'Brandname'},
            hole = 0.5
        )
        st.plotly_chart(fig1)

        st.markdown('<h1 style = "color:red;"> Total Registered Uses By State </h1>',unsafe_allow_html=True)
        mycursor.execute("""
                            SELECT State,
                                SUM(Reguser_brand) AS Total_Registered_Users,
                                AVG(Percntage) AS Average_App_Opens_Percentage
                            FROM aggregated_user  
                            GROUP BY State
                            ORDER BY Total_Registered_Users DESC
        """)
        data2 = mycursor.fetchall()
        df2 = pd.DataFrame(data2,columns = ['State','Total_Registered_Users','Average_App_Opens_Percentage'])

        fig2 = px.scatter(
            df2,
            x='Total_Registered_Users',
            y='State',
            size='Average_App_Opens_Percentage',
            title='Bubble Chart of Total Registered Users by State',
            labels={'Total_Registered_Users': 'Total Registered Users', 'State': 'State'},
            hover_name='State'  # Show state name on hover
        )
        st.plotly_chart(fig2)

        st.markdown('<h1 style = "color:green;"> Trends For App Opens By Brands </h1>',unsafe_allow_html = True)
        mycursor.execute("""
                              SELECT Year,Quater,Brandname,
                                SUM(Reguser_brand) AS Total_Registered_Users,
                                AVG(Percntage) AS Average_App_Opens_Percentage
                            FROM aggregated_user 
                            GROUP BY Year, Quater, Brandname
                            ORDER BY Average_App_Opens_Percentage desc
                            
        """)

        data3 = mycursor.fetchall()
        df3 = pd.DataFrame(data3,columns = ['Year','Quarter','Brandname','Total_Registered_Users','Average_App_Opens_Percentage'])
        

        column1,column2 = st.columns(2)
        with column1:
            yea = st.selectbox('Year',list(df3['Year'].unique()))
        with column2:
            qu = st.selectbox('Quater',list(df3['Quarter'].unique()))

        filtered_df3 = df3[(df3['Year']==yea) & (df3['Quarter'] == qu)]

        fig3 = px.line(
            filtered_df3,
            x='Brandname',
            y='Average_App_Opens_Percentage',
            title='Average App Opens Percentage by Brand',
            labels={'Average_App_Opens_Percentage': 'Average App Opens Percentage', 'Brandname': 'Brand Name'},
            markers=True  # Optional: add markers to the line
        )

        st.plotly_chart(fig3)

        st.markdown('<h1 style = "color:red;"> Trends of Brands By State Tamil Nadu </h1>',unsafe_allow_html = True)
        mycursor.execute("""
                            select State,Year,'Quater',Brandname,Reguser_brand
                            from aggregated_user
                            where State = 'tamil-nadu'
                            order by Reguser_brand desc
                         """)
        data5 = mycursor.fetchall()
        df5 = pd.DataFrame(data5,columns = ['State','Year','Quarter','Brandname','Reguser_brand'])

        year_options = df5['Year'].unique()
        select_year = st.selectbox("Select Year",year_options)

        filtered_df5 = df5[df5['Year']==select_year]


        fig5 = px.bar(
            filtered_df5,
            x = 'Brandname',
            y = 'Reguser_brand',
            title = 'Brandname By Registered User Brand',
            labels = {'Brandname':'Brandname','Reguser_brand':'Register User Brand'}
        )

        st.plotly_chart(fig5)

    
    if select_options == 'Case3':

        st.markdown('<h1 style = "color:red";> VISUALIZATION OF AGGREGATED INSURANCE </h1>',unsafe_allow_html = True)
        st.markdown('<h2 style = "color:lime";> Trend Analysis </h2>',unsafe_allow_html = True)


        mycursor.execute("""
                            SELECT 
                                State,
                                Year,
                                Quater,
                                SUM(Insurance_Count) AS Total_Insurance_Count,
                                Amount
                            FROM 
                                aggregated_insurance
                            GROUP BY 
                                State, Year,Quater,Amount
                            ORDER BY 
                                State, Year
        """)

        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State','Year','Quater','Total_Insurance_Count','Amount'])

        state_options = df['State'].unique()
        select_state = st.selectbox("Select a State",state_options)

        filtered_df = df[df['State']== select_state]
        st.subheader(f'Insurance for State,{select_state}')

        fig1 = px.pie(
            filtered_df,
            names = 'Total_Insurance_Count',
            values = 'Amount',
            title = 'Distribution of Insurance Count By Amount',
            labels={'Total_Insurance_Count'},
            hole = 0.5
        )
        st.plotly_chart(fig1)


        st.markdown('<h1 style = "color:blue";> Insurance By Year </h1>',unsafe_allow_html = True)


        mycursor.execute("""
                            select Year,Quater,sum(Insurance_Count) as total_count
                            from aggregated_insurance
                            group by  Year,Quater
                            order by total_count
        """)

        data1 = mycursor.fetchall()
        df1 = pd.DataFrame(data1,columns = ['Year','Quater','total_count'])

        year_options = df1['Year'].unique()
        select_year = st.selectbox("Select a Year",year_options)


        filtered_df1 = df1[df1['Year']== select_year]
        st.subheader(f'Insurance for Year,{select_year}')

        fig1 = px.line(
            filtered_df1,
            x='Quater',
            y='total_count',
            title=f'Top Insurance by Year {select_year}',
            labels={'Quater': 'Quarter', 'total_count': 'Total Count'},
            markers=True  # Add markers to the line
        )

        # Update the layout for better visibility
        fig1.update_traces(marker=dict(size=10, color='darkviolet'))
        st.plotly_chart(fig1)
        

        st.markdown('<h1 style = "color:red;"> Insurance by State and Amount </h1>',unsafe_allow_html = True)
        mycursor.execute("""
                            select state,Insurance_Count,Amount
                            from aggregated_insurance
        """)
        data2 = mycursor.fetchall()
        df2 = pd.DataFrame(data2,columns = ['state','Insurance_Count','Amount'])
        state_options = df2['state'].unique()
        select_state = st.selectbox('Select a state',state_options)
        filtered_df2 = df2[df2['state'] == select_state]

        fig2 = px.bar(
            filtered_df2,
            x = 'Insurance_Count',
            y = 'Amount',
            text = 'Amount',
            title = f'Transaction Distribution {select_state.capitalize()}',
            labels = {'Insurance_Count':'Insurance Count','Amount':'Total Amount'},
            
        )
        fig2.update_traces(texttemplate = '%{text:.2s}',textposition='outside',marker_color = 'blue')
        st.plotly_chart(fig2)

        st.markdown('<h1 style = "color:red;"> Year By Quater  </h1>',unsafe_allow_html = True)
        mycursor.execute("""
                            select state,year,quater,
                sum(Amount) as total_transaction_amount
                from aggregated_insurance where year = 2020 and quater = 3
                group by state
                order by total_transaction_amount
        """)
        data3 = mycursor.fetchall()
        df3 = pd.DataFrame(data3,columns = ['state','year','quater','total_transaction_amount'])
        

        fig3 = px.line(
            df3,
            x = 'state',
            y = 'total_transaction_amount',
            title = f'State by Amount',
            labels = {'state':'State','total_transaction_amount':'Total Transaction Amount'},
            markers = True
        )
        st.plotly_chart(fig3)


    if select_options == 'Case4':
        st.markdown('<h1 style = "color:red;"> VISUALIZATION FOR MAP TRANSACTION </h1>',unsafe_allow_html=True)
        st.markdown('<h2 style = "color:blue;">Transaction Amount By State Sikkim </h2>',unsafe_allow_html=True)

        mycursor.execute("""
                             select * from map_transaction where state = 'sikkim'
        """)
        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State','Year','Quater','district_name','Transaction_Count','Transaction_Amount'])
        column1,column2 = st.columns(2)
        with column1:
            ye = st.selectbox('Year',list(df['Year'].unique()))
        with column2:
            qu = st.selectbox('Quarter',list(df['Quater'].unique()))

        filtered_df = df[(df['Year']==ye) & (df['Quater']==qu)]

        fig = px.bar(
            filtered_df,
            x = 'district_name',
            y = 'Transaction_Count',
            text = 'Transaction_Count',
            title = 'District Name By Transaction Count',
            labels = {'district_name':'District Name','Transaction_Count':'Transaction Count'}
        )
        fig.update_traces(texttemplate = '%{text:.2s}',textposition='outside',marker_color = 'green')
        st.plotly_chart(fig)

        st.markdown('<h1 style = "color:red;"> Top State By Transaction Amount  </h1>',unsafe_allow_html = True)
        mycursor.execute("""
                             select state,year,quater,
                sum(Transaction_Amount) as total_trans_amount
                from map_transaction where year = 2018 and quater = 1
                group by state
                order by total_trans_amount
        """)
        data1 = mycursor.fetchall()
        df1 = pd.DataFrame(data1,columns = ['state','year','quater','total_trans_amount'])
        

        fig1 = px.line(
            df1,
            x = 'state',
            y = 'total_trans_amount',
            title = f'State by Amount',
            labels = {'state':'State','total_trans_amount':'Total Transaction Amount'},
            markers = True
        )
        st.plotly_chart(fig1)

        st.markdown('<h1 style = "color:red;"> TRENDS OF TRANSACTION COUNTS</h1>',unsafe_allow_html = True)
        mycursor.execute("""
                        select distinct state, sum(Transaction_Count) as total_counts from map_transaction
                        group by state
                        order by sum(Transaction_Count)  desc limit 15
                         """)
        
        data2 = mycursor.fetchall()
        df2 = pd.DataFrame(data2,columns = ['state','total_counts'])

        fig2 = px.pie(
            df2,
            names = 'state',
            values = 'total_counts',
            title = 'Transaction Counts By State',
            labels = 'state',
            hole = 0.4
        )

        st.plotly_chart(fig2)


        st.markdown('<h1 style = "color:blue;"> Top 10 State Wise Total Transaction Amount </h1>',unsafe_allow_html = True)
        mycursor.execute("""
                         select State,
                         sum(Transaction_Amount) as total_amount
                         from map_transaction
                         group by state
                         order by total_amount desc
                         limit 10""")
        data3 = mycursor.fetchall()
        df3 = pd.DataFrame(data3,columns = ['state','total_amount'])

        fig3 = px.bar(
            df3,
            x = 'state',
            y = 'total_amount',
            text = 'total_amount',
            title = 'Total Transaction Amount by State',
            labels = {'state':'State','total_amount':'Total Amount'}
            
            )
        fig3.update_traces(texttemplate ='%{text:.2s}', textposition = 'outside',marker_color='purple')
        st.plotly_chart(fig3)


        st.markdown('<h1 style = "color:blue;"> Trend Analysis </h1>',unsafe_allow_html = True)
        mycursor.execute("""
                            select year,quater,
                            sum(Transaction_Count)  as total_transaction_count,
                            sum(Transaction_Amount) as total_amount
                            from map_transaction
                            group by year,quater
                            order by year,quater
        """)
        data4 = mycursor.fetchall()
        df4 = pd.DataFrame(data4,columns = ['year','quater','total_transaction_count','total_amount'])

        year_option = df4['year'].unique()
        select_year = st.selectbox("Select a Year" , year_option)

        filtered_df4 = df4[df4['year'] == select_year]
        st.subheader(f'Transactions for Year {select_year}')

        plt.figure(figsize = (4,2))
        plt.bar(filtered_df4['quater'].astype(str),filtered_df4['total_amount'],color = 'blue',width = 0.5)
        plt.xlabel('Quater')
        plt.ylabel('Total Transaction Amount')
        plt.title(f'Transaction Amount Distribution for {select_year}')
        plt.xticks(rotation = 0)
        
        st.pyplot(plt)

    if select_options == 'Case5':
        st.markdown('<h1 style = "color:red";> VISUALIZATION OF MAP USER </h1>',unsafe_allow_html = True)
        st.markdown('<h2 style = "color:lime";> Trend Analysis </h2>',unsafe_allow_html = True)


        mycursor.execute("""
                            SELECT State,
                                SUM(Registereduser) AS Total_Registered_Users    
                            FROM map_user 
                            GROUP BY State
                            ORDER BY Total_Registered_Users desc
                           
        """)

        data = mycursor.fetchall()
        df = pd.DataFrame(data,columns = ['State','Total_Registered_Users'])

        fig = px.bar(
            df,
            x = 'State',
            y = 'Total_Registered_Users',
            text = 'Total_Registered_Users',
            title = 'State Registered User',
            labels = {'State': 'State','Total_Registered_Users':'Registered User'}
        )
        fig.update_traces(texttemplate = '%{text:.2s}',textposition='outside',marker_color = 'darkviolet')
        st.plotly_chart(fig)

        st.markdown('<h1 style = "color:blue;"> Top State By App opens</h1>',unsafe_allow_html = True)
        mycursor.execute("""
                        SELECT  distinct State,
								SUM(Registereduser) AS Total_Registered_Users,
                                AVG(Apps) AS Average_App
                            FROM map_user  
                            GROUP BY State
                            ORDER BY Average_App DESC
                            limit 10
                         """)
        
        data2 = mycursor.fetchall()
        df2 = pd.DataFrame(data2,columns = ['state','Total_Registered_Users','Average_App'])

        fig2 = px.pie(
            df2,
            names = 'state',
            values = 'Average_App',
            title = ' Average App opens By State',
            labels = 'state',
            hole = 0.4
        )

        st.plotly_chart(fig2)

        st.markdown('<h1 style = "color:red;"> Quater And Year Wise App Opens For puducherry</h1>',unsafe_allow_html = True)
        mycursor.execute("""
                            select state,year,Quater,sum(Registereduser) as total_Registered_User
                            from map_user
                            where state = 'puducherry'
                            group by state,year,Quater
                            order by total_Registered_User
                         
        """)
        data3 = mycursor.fetchall()
        df3 = pd.DataFrame(data3,columns = ['state','Year','Quater','total_Registered_User'])
        quater_option = df3['Quater'].unique()
        select_quater= st.selectbox("Select a Quater" , quater_option)

        filtered_df4 = df3[df3['Quater'] == select_quater]

        # Create a line chart
        fig2 = px.line(
            filtered_df4,
            x='Year',
            y='total_Registered_User',
            text='total_Registered_User',
            title='Total Registered Users Over Years',
            labels={'Year': 'Year', 'total_Registered_User': 'Total Registered Users'},
            markers=True  # Adding  markers to the line
        )
        fig2.update_traces(texttemplate='%{text:.2s}', textposition='top center', marker_color='blue')
        st.plotly_chart(fig2)

        