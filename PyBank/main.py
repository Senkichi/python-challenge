#!/usr/bin/env python
# coding: utf-8

# In[92]:


import pandas as pd



bank_df = pd.read_csv('budget_data.csv')


# In[11]:


bank_df.head()


# In[78]:


num_months = bank_df['Date'].nunique()
num_months


# In[79]:


net_change = bank_df['Profit/Losses'].sum()
net_change


# In[ ]:


increase = 0
decrease = 0
diff_list = []
counter = 0
for row in range(len(bank_df)):
    counter = counter + 1
    current = bank_df['Profit/Losses'][row]
    future = bank_df['Profit/Losses'][row + 1]
    difference = future - current
    diff_list.append(difference)
    if difference > increase:
        increase = difference
        up_month = bank_df['Date'][row + 1]
    if difference < decrease:
        decrease = difference
        down_month = bank_df['Date'][row + 1]
    if counter == 85:
        break
    
    


# In[93]:





# In[98]:


print('Financial Analysis')
print("------------------------------------------------------------------------")
print('Total Months: ' + str(num_months))
print('Total: ' + '$' + str(net_change))
print('Average Change: ' + '$' + str(sum(diff_list)/len(diff_list)))
print('Greatest Increase in Profits: ' + up_month)
print('Greatest Decrease in Profits: ' + down_month)


# In[99]:


pybank = open('PyBank.txt','w')
pybank.write('Financial Analysis' + '\n' + 'Total Months: ' + str(num_months) + '\n' + 'Total: ' + '$' + str(net_change) +
       '\n' + 'Average Change: ' + '$' + str(sum(diff_list)/len(diff_list)) + '\n' + 'Greatest Increase in Profits: ' + up_month +
       '\n' + 'Greatest Decrease in Profits: ' + down_month)
pybank.close()


# In[ ]:




