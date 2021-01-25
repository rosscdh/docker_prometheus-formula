def test_file_exists(host):
    docker_prometheus = host.file('/docker_prometheus.yml')
    assert docker_prometheus.exists
    assert docker_prometheus.contains('your')

# def test_docker_prometheus_is_installed(host):
#     docker_prometheus = host.package('docker_prometheus')
#     assert docker_prometheus.is_installed
#
#
# def test_user_and_group_exist(host):
#     user = host.user('docker_prometheus')
#     assert user.group == 'docker_prometheus'
#     assert user.home == '/var/lib/docker_prometheus'
#
#
# def test_service_is_running_and_enabled(host):
#     docker_prometheus = host.service('docker_prometheus')
#     assert docker_prometheus.is_enabled
#     assert docker_prometheus.is_running
