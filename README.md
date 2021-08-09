# montana-fly-fishing-report
Alexa App build for Montana fly fishing report

(this still kind of a work in progess.)


Currently scraping fishing conditions from 
https://troutfitters.com/fishing-reports

## List of Montana rivers
1. Gallatin River
1. Lower Madison River
1. Upper Madison River
1. Yellowstone River
1. Springs Creek
1. Jefferson River
1. Big Hole
1. Boulder River
1. Stillwater River
1. Bighorn River
1. Missouri River
1. Yellowstone Park Waters
1. Other waters

## How it works
###  The basics
1) scrape.py scapes fly fishing site and creates text file
2) uploads text to S3
3) from there Lamba coverts text to mp3 using AWS Polly
4) Alexa use coverted mp3 


https://aws.amazon.com/blogs/machine-learning/build-your-own-text-to-speech-applications-with-amazon-polly/

## application acrchitecture

### create a dynamodb table
create dynamodb tables

table name
    montana-fly-fishing-report-post
primary key
    id

table sturcture 
    id – The ID of the post
    status – UPDATED or PROCESSING, depending on whether an MP3 file has already been created
    text – The post’s text, for which an audio file is being created
    url – A link to an S3 bucket where an audio file is being stored
    voice – The Amazon Polly voice that was used to create audio file

### create s3 bucket
create s3 bucket

bucket policy

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "ARN here/*"
    }
  ]
}

### create an sns topic

### Creating mp4
( create a script in lambda )
1. Upload txt file to s3
1. Tiggers lambda to polly
1. Polly to S3

### Alexa App
node

