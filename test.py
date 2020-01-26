def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--region', type=str, required='True', help='the region')
  args = parser.parse_args()

  ec2 = boto3.setup_default_session(region_name=args.region)
  asgclient = boto3.client('autoscaling')

  message = {}
  data = list_asg(asgclient)
  if data:
     pprint.pprint(data)
     mark_unHealthy(asgclient, data)

if __name__ == '__main__':
   main()
