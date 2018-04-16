#import workspace from Azure, set up the data frame
from azureml import Workspace
ws = Workspace()
experiment = ws.experiments['aad1200b3a5a422d8e75a41f9fcc1299.f-id.a8cddcb61b594851ad21466102f6e92f']
ds = experiment.get_intermediate_dataset(
    node_id='21e15cc1-15b7-4bc4-8f93-923ea9fe55e3-207',
    port_name='Results dataset',
    data_type_id='GenericCSV'
)
frame = ds.to_dataframe()

#visualize the data to plot every point against every point
%matplotlib inline

import seaborn as sns
num_cols = ["mood (num)","sleep","sleep (2)","miles","total cal"]
sns.pairplot(frame[num_cols], size=2)
