FROM prefecthq/prefect:0.15.6-python3.7
RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /opt/prefect
#COPY flow_utilities/ /opt/prefect/flow_utilities/
ADD . .
#COPY requirements.txt .
#COPY setup.py .
RUN pip install .
#COPY workflow/ /opt/prefect/workflow/
#COPY components/ /opt/prefect/components/