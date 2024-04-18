# Increases the amount of traffic for Nginx server.

# change the default limit of nginx server
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'sudo nginx restart',
  path    => '/etc/init.d/'
}
