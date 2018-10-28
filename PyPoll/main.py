#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd


# In[23]:


poll_df = pd.read_csv('election_data.csv')
poll_df.head()


# In[24]:


num_votes = poll_df['Voter ID'].nunique()
num_votes


# In[25]:


candidates = poll_df['Candidate'].unique()
candidates


# In[26]:


khan_pct = (len(poll_df[poll_df['Candidate'] == 'Khan'])/len(poll_df['Candidate']))*100
khan_pct
correy_pct = (len(poll_df[poll_df['Candidate'] == 'Correy'])/len(poll_df['Candidate']))*100

li_pct = (len(poll_df[poll_df['Candidate'] == 'Li'])/len(poll_df['Candidate']))*100

otooley_pct = (len(poll_df[poll_df['Candidate'] == "O'Tooley"])/len(poll_df['Candidate']))*100


# In[27]:


khan_count = len(poll_df[poll_df['Candidate'] == 'Khan'])
correy_count = len(poll_df[poll_df['Candidate'] == 'Correy'])
li_count = len(poll_df[poll_df['Candidate'] == 'Li'])
otooley_count = len(poll_df[poll_df['Candidate'] == "O'Tooley"])


# In[28]:


poll_df['Candidate'].value_counts()


# In[30]:


print('Election Results')
print("------------------------------------------------------------------------")
print('Total Votes: ' + str(num_votes))
print("------------------------------------------------------------------------")
print('Khan: ' + str(khan_pct) + '%' + ' (' + str(khan_count) + ')')
print('Correy: ' + str(correy_pct) + '%' + ' (' + str(correy_count) + ')')
print('Li: ' + str(li_pct) + '%' + ' (' + str(li_count) + ')')
print("O'Tooley: " + str(otooley_pct) + '%' + ' (' + str(otooley_count) + ')')
print("------------------------------------------------------------------------")
print('Winner: Khan')





pypoll = open('PyPoll.txt','w')
pypoll.write('Election Results' + '\n' + 'Total Votes: ' + str(num_votes) + '\n' +
             "------------------------------------------------------------------------" + '\n' +
             'Khan: ' + str(khan_pct) + '%' + ' (' + str(khan_count) + ')' + '\n' +
             'Correy: ' + str(correy_pct) + '%' + ' (' + str(correy_count) + ')' + '\n' +
             'Li: ' + str(li_pct) + '%' + ' (' + str(li_count) + ')' + '\n' + 
             "O'Tooley: " + str(otooley_pct) + '%' + ' (' + str(otooley_count) + ')' + '/n' +
             "------------------------------------------------------------------------" + '\n' +
             'Winner: Khan')
pypoll.close()


# In[ ]:




